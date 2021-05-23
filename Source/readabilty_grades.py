# from .constants import FIRST_CONSTANT
FIRST_CONSTANT = 11.8


def kincaid_grade_level(total_syllables, total_words, total_sentences) -> float:
    """
    Calculates readability score using the Flesch-Kincaid Grade Level.
    The Flesch-Kincaid Grade Level is equivalent to the US grade level of education.
    It shows the required education to be able to understand a text.
    :param total_syllables: total amount of syllables in the text
    :param total_words: total amount of words in the text
    :param total_sentences: total amount of sentences in the text
    :return:
    """
    return 0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59


def flesch_reading_ease(total_syllables, total_words, total_sentences):
    """
    Calculates readability score using the Flesh-Kincaid Reading Ease.
    The higher the reading score, the easier a piece of text is to read.
    :param total_syllables: total amount of syllables in the text
    :param total_words: total amount of words in the text
    :param total_sentences: total amount of sentences in the text
    :return:
    """
    return 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)


def ari(characters, words, sentences):
    """

    :param characters:
    :param words:
    :param sentences:
    :return:
    """
    return 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43


def coleman_liau_index(characters, words, sentences):
    """

    :param characters:
    :param words:
    :param sentences:
    :return:
    """
    return (5.879851 * characters / words - 29.587280 * sentences / words
            - 15.800804)


def gunning_fox_index(words, complex_words, sentences):
    """

    :param words:
    :param complex_words:
    :param sentences:
    :return:
    """
    return 0.4 * ((words / sentences) + (100 * (complex_words / words)))