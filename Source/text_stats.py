from __future__ import division, print_function, unicode_literals
from typing import Iterable, List
try:
    import re2 as re
except ImportError:
    import re
from syllables_counter import LANGDATA
from readabilty_grades import kincaid_grade_level, ari, coleman_liau_index, flesch_reading_ease, gunning_fox_index
from nltk.probability import FreqDist


def get_words_freq(word_tokens: list) -> list:
    """

    :param word_tokens:
    :return:
    """
    fdist = FreqDist(word_tokens)
    top_ten = fdist.most_common(10)
    return top_ten


# Returns a quantity of paragraphs present in a text.
def get_paragraphs_count(raw_text: Iterable[str]) -> int:
    """

    :param raw_text:
    :return:
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


# Filters word tokens by removing special symbols.
# Returns filtered list of word tokens.
def word_token_filter(word_token):
    """

    :param word_token:
    :return:
    """
    # list comprehensions!!!!
    word_token_filtered = [word for word in word_token if word.isalnum()]


    # for word in wordToken:
    #     for char in word:
    #         if not char.isalnum():
    #             word = word.replace(char, "")
    #
    #     if word.isalnum():
    #         word_token_filtered.append(word)

    return word_token_filtered


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
def get_parts_of_speech(tagged_word_tokens: list) -> dict:
    """

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


# Makes all necessary text measures.
# Returns an ordered dictionary.
def get_measures(parsed_text: list) -> dict:
    """

    :param parsed_text:
    :return:
    """
    characters = 0
    total_syllables = 0
    complex_words = 0
    long_words = 0
    unique_words = set()
    syllables_counter = LANGDATA['syllables']

    if isinstance(parsed_text, bytes):
        raise ValueError('Expected: unicode string or an iterable of lines')

    paragraphs = get_paragraphs_count(parsed_text['rawText'])
    total_sentences = len(parsed_text['sentToken'])
    filtered_word_tokens = word_token_filter(parsed_text['wordToken'])
    parts_of_speech = get_parts_of_speech(parsed_text['tagged'])
    total_words = len(filtered_word_tokens)
    words_frequency = get_words_freq(filtered_word_tokens)

    for word_token in filtered_word_tokens:
        unique_words.add(word_token)
        characters += len(word_token)
        syllable = syllables_counter(word_token)
        total_syllables += syllable
        if len(word_token) >= 7:  # TODO: magic number!! Can be in another function
            long_words += 1

        if syllable >= 3 and not word_token[0].isupper():  # TODO: magic number!!
            complex_words += 1

    if not total_words:
        raise ValueError("I can't do this, there's no words there!")

    stats = dict([
        ('Average number of characters per word', characters / total_words),
        ('Average number of syllables per word', total_syllables / total_words),
        ('Average number of words per sentence', total_words / total_sentences),
        ('Sentences per paragraph', total_sentences / paragraphs),
        ('Number of characters (without spaces)', characters),
        ('Syllables', total_syllables),
        ('Number of words', total_words),
        ('Unique words', len(unique_words)),
        ('Number of sentences', total_sentences),
        ('Number of paragraphs', paragraphs),
        ('Number of long words', long_words),
        ('Number of complex words', complex_words),
        ('Words frequency', words_frequency)
    ])
    readability = dict([
        ('Kincaid', kincaid_grade_level(total_syllables, total_words, total_sentences)),
        ('ARI', ari(characters, total_words, total_sentences)),
        ('Coleman-Liau',
         coleman_liau_index(characters, total_words, total_sentences)),
        ('Flesch Reading Ease',
         flesch_reading_ease(total_syllables, total_words, total_sentences)),
        ('Gunning Fog Index',
         gunning_fox_index(total_words, complex_words, total_sentences))
    ])
    print(type(readability['Kincaid']))
    return dict([
        ('READABILITY GRADES', readability),
        ('TEXT INFO', stats),
        ('PARTS OF SPEECH', parts_of_speech)
    ])