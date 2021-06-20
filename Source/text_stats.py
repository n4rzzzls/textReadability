from typing import List, Dict
from readabilty_grades import kincaid_grade_level, ari, coleman_liau_index, flesch_reading_ease, gunning_fog_index
from nltk.probability import FreqDist
import re
from constants import GRADES_RANGE as gr, COMPLEX_WORD_SYLLABLES, LONG_WORD_SYLLABLES


def get_sentence_count(sentence_tokens: List[str]) -> int:
    return len(sentence_tokens)


def get_syllables_counter(word: str) -> int:
    """
    Counts the amount of syllables in the word
    :param word: word to be used for counting
    :return: the amount of syllables in the word
    """
    # word = word.lower()
    # count = 0
    # vowels = "aeiouy"
    # if word[0] in vowels:
    #     count += 1
    # for index in range(1, len(word)):
    #     if word[index] in vowels and word[index - 1] not in vowels:
    #         count += 1
    # if word.endswith("e") and not word.endswith("le"):
    #     count -= 1
    # if count == 0:
    #     count += 1

    word = word if type(word) is str else str(word)

    word = word.lower()

    if len(word) <= 3:
        return 1
    # import pdb; pdb.set_trace()
    word = re.sub('(?:[^laeiouy]es|[^laeiouy]e)$', '', word)
    word = re.sub('^y', '', word)
    matches = re.findall('[aeiouy]{1,2}', word)
    count = len(matches)

    return count


def get_words_freq(word_tokens: List[str]) -> List[tuple[str, int]]:
    """
    Finds a 10 most used words in the text
    :param word_tokens: word tokens
    :return: list of 10 used words in the text
    """
    fdist = FreqDist(word_tokens)
    top_ten = fdist.most_common(10)
    return top_ten


def get_words_count(filtered_word_tokens: List[str]) -> int:
    return len(filtered_word_tokens)


def get_characters_count(word_tokens: List[str]) -> int:
    """
    Counts the amount of characters in the text
    :param word_tokens:
    :return:
    """
    characters = 0

    for word in word_tokens:
        for symbol in word:
            if symbol.isalpha():
                characters += 1

    return characters


FILTERED_SYMBOLS = (
    ',',
    '.',
    '!',
    '?',
    '\'',
    '`',
    '\"',
    '``',
    '\'\''
)


def word_token_filter(tagged_word_tokens: List[str]) -> List[str]:
    """
    Filters word tokens.
    :param tagged_word_tokens: list of tagged word tokens
    :return: filtered list of word tokens
    """

    word_tokens_filtered = []

    for tagged_word_token in tagged_word_tokens:
        word_token, word_tag = tagged_word_token

        if word_tag == 'POS':
            word_tokens_filtered[len(word_tokens_filtered) - 1] += word_token
            continue

        if word_token in FILTERED_SYMBOLS:
            continue

        if word_token.isdecimal():
            continue

        if word_token.find('-') != -1:
            x = word_token.split('-')

            for y in x:
                word_tokens_filtered.append(y)
            continue

        word_tokens_filtered.append(word_token)

    return word_tokens_filtered


TAG_WORD_CATEGORY_MAPPING = {
    'PRP': 'Pronouns',
    'PRP$': 'Pronouns',
    'MD': 'Modals',
    'CC': 'Conjunctions',
    'FW': 'Foreign words',
    'IW': 'Prepositions',
    'CD': 'Cardinal digits',
    'RB': 'Adverbs',
    'RBR': 'Adverbs',
    'RBS': 'Adverbs',
    'VB': 'Verbs',
    'VBG': 'Verbs',
    'VBD': 'Verbs',
    'VBN': 'Verbs',
    'VBP': 'Verbs',
    'VBZ': 'Verbs',
    'NN': 'Nouns',
    'NNS': 'Nouns',
    'NNP': 'Nouns',
    'NNPS': 'Nouns'
}


def get_parts_of_speech(tagged_word_tokens: list) -> Dict[str, int]:
    """
    Distributes the words amongst parts of speech
    :param tagged_word_tokens:
    :return:
    """
    words = dict([
        ("Pronouns", 0),
        ("Modals", 0),
        ("Conjunctions", 0),
        ("Foreign words", 0),
        ("Prepositions", 0),
        ("Cardinal digits", 0),
        ("Adverbs", 0),
        ("Verbs", 0),
        ("Nouns", 0)
    ])

    for _, tag in tagged_word_tokens:
        if tag in TAG_WORD_CATEGORY_MAPPING:
            words[TAG_WORD_CATEGORY_MAPPING[tag]] += 1

    return words


def get_absolute_score(kincaid: list, flesch: list, ari_: list, coleman: list, fog: list) -> int:
    """
    Calculates absolute readability value
    :return: The absolute readability value
    """
    kincaid, _ = kincaid
    flesch, _ = flesch
    ari_, _ = ari_
    coleman, _ = coleman
    fog, _ = fog

    result = round(100 * (kincaid / gr['kincaid'] + flesch / gr['flesch'] + ari_ / gr['ari'] + coleman / gr['coleman']
                          + fog / gr['fog']) / 5)

    return result


def get_text_measures(parsed_text: dict) -> dict:
    """
    Performs all necessary text measures
    :param parsed_text: parsed text
    :return: readability grades, text statistics and parts of speech
    """
    total_syllables = 0
    total_complex_words = 0
    total_long_words = 0
    total_unique_words = set()

    filtered_word_tokens = word_token_filter(parsed_text['tagged'])
    total_sentences = get_sentence_count(parsed_text['sentence_tokens'])
    parts_of_speech = get_parts_of_speech(parsed_text['tagged'])
    total_words = get_words_count(filtered_word_tokens)
    words_frequency = get_words_freq(filtered_word_tokens)
    total_characters = get_characters_count(parsed_text['word_tokens'])

    for word_token in filtered_word_tokens:
        total_unique_words.add(word_token)
        syllable = get_syllables_counter(word_token)
        total_syllables += syllable

        if len(word_token) >= LONG_WORD_SYLLABLES:
            total_long_words += 1

        if syllable >= COMPLEX_WORD_SYLLABLES and not word_token[0].isupper():
            total_complex_words += 1

    if not total_words:
        raise ValueError("I can't do this, there's no words there!")

    characters_per_word = total_characters / total_words
    syllables_per_word = total_syllables / total_words
    word_per_sentence = total_words / total_sentences
    kincaid = kincaid_grade_level(total_syllables, total_words, total_sentences)
    ari_ = ari(total_characters, total_words, total_sentences)
    coleman_liau = coleman_liau_index(total_characters, total_words, total_sentences)
    flesch = flesch_reading_ease(total_syllables, total_words, total_sentences)
    fog = gunning_fog_index(total_words, total_complex_words, total_sentences)
    absolute_score = get_absolute_score(kincaid, ari_, coleman_liau, flesch, fog)
    print("-" * 20, '\n', "ABSOLUTE READABILITY", "\n", "-" * 20)
    print(f"Text has {absolute_score} general score")

    stats = dict([
        ('Average number of characters per word', characters_per_word),
        ('Average number of syllables per word', syllables_per_word),
        ('Average number of words per sentence', word_per_sentence),
        ('Number of characters', total_characters),
        ('Syllables', total_syllables),
        ('Number of words', total_words),
        ('Unique words', len(total_unique_words)),
        ('Number of sentences', total_sentences),
        ('Number of long words', total_long_words),
        ('Number of complex words', total_complex_words),
        ('Words frequency', words_frequency)
    ])

    readability_grades = dict([
        ('Kincaid', kincaid),
        ('ARI', ari_),
        ('Coleman-Liau', coleman_liau),
        ('Flesch Reading Ease', flesch),
        ('Gunning Fog Index', fog)
    ])

    return dict([
        ('READABILITY GRADES', readability_grades),
        ('TEXT INFO', stats),
        ('PARTS OF SPEECH', parts_of_speech)
    ])
