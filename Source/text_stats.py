from __future__ import division, print_function, unicode_literals
from typing import List, Dict
from utils import is_word_long
from readabilty_grades import kincaid_grade_level, ari, coleman_liau_index, flesch_reading_ease, gunning_fog_index
from nltk.probability import FreqDist
try:
    import re2 as re
except ImportError:
    import re


def get_syllables_counter(word: str) -> int:
    """
    Counts the amount of syllables in the word
    :param word: word to be used for counting
    :return: the amount of syllables in the word
    """
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e") and not word.endswith("le"):
        count -= 1
    if count == 0:
        count += 1
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


def get_paragraphs_count(raw_text: List[str]) -> int:
    """
    Calculates the quantity of paragraphs present in a text
    :param raw_text: raw text from input file
    :return: quantity of paragraphs
    """
    paragraphs = 1

    is_newline = False
    for sent in raw_text:
        if is_newline and sent == "\n":
            paragraphs += 1
            is_newline = False
        elif sent == "\n":
            is_newline = True
            continue
    return paragraphs


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


# Returns dictionary with words usage: nouns, adverbs and so on
def get_parts_of_speech(tagged_word_tokens: List) -> Dict[str, int]:
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

    total_paragraphs = get_paragraphs_count(parsed_text['raw_text'])
    total_sentences = len(parsed_text['sentence_tokens'])
    filtered_word_tokens = word_token_filter(parsed_text['tagged'])
    parts_of_speech = get_parts_of_speech(parsed_text['tagged'])
    total_words = len(filtered_word_tokens)
    words_frequency = get_words_freq(filtered_word_tokens)
    total_characters = get_characters_count(parsed_text['word_tokens'])

    for word_token in filtered_word_tokens:
        total_unique_words.add(word_token)
        syllable = get_syllables_counter(word_token)
        total_syllables += syllable

        if is_word_long(word_token):
            total_long_words += 1

        if syllable >= 3 and not word_token[0].isupper():  # TODO: magic number!!
            total_complex_words += 1

    if not total_words:
        raise ValueError("I can't do this, there's no words there!")

    characters_per_word = total_characters / total_words
    syllables_per_word = total_syllables / total_words
    word_per_sentence = total_words / total_sentences
    sentences_per_paragraph = total_sentences / total_paragraphs

    stats = dict([
        ('Average number of characters per word', characters_per_word),
        ('Average number of syllables per word', syllables_per_word),
        ('Average number of words per sentence', word_per_sentence),
        ('Sentences per paragraph', sentences_per_paragraph),
        ('Number of characters', total_characters),
        ('Syllables', total_syllables),
        ('Number of words', total_words),
        ('Unique words', len(total_unique_words)),
        ('Number of sentences', total_sentences),
        ('Number of paragraphs', total_paragraphs),
        ('Number of long words', total_long_words),
        ('Number of complex words', total_complex_words),
        ('Words frequency', words_frequency)
    ])

    readability = dict([
        ('Kincaid', kincaid_grade_level(total_syllables, total_words, total_sentences)),
        ('ARI', ari(total_characters, total_words, total_sentences)),
        ('Coleman-Liau',
         coleman_liau_index(total_characters, total_words, total_sentences)),
        ('Flesch Reading Ease',
         flesch_reading_ease(total_syllables, total_words, total_sentences)),
        ('Gunning Fog Index',
         gunning_fog_index(total_words, total_complex_words, total_sentences))
    ])

    return dict([
        ('READABILITY GRADES', readability),
        ('TEXT INFO', stats),
        ('PARTS OF SPEECH', parts_of_speech)
    ])
