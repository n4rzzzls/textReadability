from constants import COLEMAN_LIAU_INDEX_CONSTANTS, ARI_CONSTANTS, \
    GUNNING_FOX_INDEX_CONSTANTS, KINCAID_GRADE_LEVEL_CONSTANTS, \
    FLESH_READING_EASE_CONSTANTS


KINCAID_GRADE_LEVELS = {
    'Easy to read': range(0, 5, 1),
    'Medium difficulty': range(6, 11, 1),
    'Hard to read': range(12, 100, 1)
}


FLESH__READING_EASE_LEVELS = {
    'Extremely difficult to read. Best understood by university graduates': range(0, 10, 1),
    'Very difficult to read. Best understood by university graduates': range(11, 30, 1),
    'Difficult to read': range(31, 50, 1),
    'Fairly difficult to read': range(51, 60, 1),
    'Plain English. Easily understood by 13- to 15-year-old students': range(61, 70, 1),
    'Fairly easy to read': range(71, 80, 1),
    'Easy to read. Conversational English for consumers': range(81, 80, 1),
    'Very easy to read. Easily understood by an average 11-year-old student': range(91, 100, 1)
}

ARI_LEVELS = {

}


COLEMAN_LIAU_INDEX_LEVELS = {

}


GUNNING_FOX_INDEX_LEVELS ={

}


def kincaid_grade_level(total_syllables: float, total_words: float, total_sentences: float) -> dict:
    """
    Calculates readability score using the Flesch-Kincaid Grade Level.
    The Flesch-Kincaid Grade Level is equivalent to the US grade level of education.
    It shows the required education to be able to understand a text.
    :param total_syllables: total amount of syllables in the text
    :param total_words: total amount of words in the text
    :param total_sentences: total amount of sentences in the text
    :return: grade level
    """
    readability_score = round(
        KINCAID_GRADE_LEVEL_CONSTANTS['FIRST'] * (total_words / total_sentences) + KINCAID_GRADE_LEVEL_CONSTANTS[
            'SECOND'] * (total_syllables / total_words) - KINCAID_GRADE_LEVEL_CONSTANTS['THIRD'])

    for readability_level, score in KINCAID_GRADE_LEVELS.items():

        if readability_score in score:
            readability_result = [readability_score, readability_level]

    return readability_result


def flesch_reading_ease(total_syllables: float, total_words: float, total_sentences: float) -> float:
    """
    Calculates readability score using the Flesh-Kincaid Reading Ease.
    The higher the reading score, the easier a piece of text is to read.
    :param total_syllables: total amount of syllables in the text
    :param total_words: total amount of words in the text
    :param total_sentences: total amount of sentences in the text
    :return: reading ease score
    """

    readability_score = round(FLESH_READING_EASE_CONSTANTS['FIRST'] - (FLESH_READING_EASE_CONSTANTS['SECOND'] * (
            total_words / total_sentences)) - (FLESH_READING_EASE_CONSTANTS['THIRD'] * (total_syllables / total_words)))

    for readability_level, score in FLESH__READING_EASE_LEVELS.items():
        if readability_score in score:
            readability_result = [readability_score, readability_level]

    return readability_result


def ari(total_characters: float, total_words: float, total_sentences: float) -> float:
    """
    Calculates readability score using the Automated Readability Index.
    The ARI assesses the U.S. grade level required to read a piece of text.
    In some ways, it is similar to other formulas. Its difference is rather than counting syllables, it counts
    characters. The more characters, the harder the word. It also counts sentences. This sets it apart from some other
    formulas.
    :param total_characters: total amount of characters in the text
    :param total_words: total amount of words in the text
    :param total_sentences: total amount of sentences in the text
    :return: readability index. The higher the harder the text is to read
    """

    readability_score = round(ARI_CONSTANTS['FIRST'] * (total_characters / total_words) + ARI_CONSTANTS[
        'SECOND'] * (total_words / total_sentences) - ARI_CONSTANTS['THIRD'])

    for readability_level, score in ARI_LEVELS.items():
        if readability_score in score:
            readability_result = [readability_score, readability_level]

    return readability_result


def coleman_liau_index(total_characters: float, total_words: float, total_sentences: float) -> float:
    """
    Calculates readability score using the Coleman Liau Index.
    :param total_characters: total amount of characters in the text
    :param total_words: total amount of words in the text
    :param total_sentences: total amount of sentences in the text
    :return: Coleman Liau Index
    """

    readability_score = round(
        COLEMAN_LIAU_INDEX_CONSTANTS['FIRST'] * (total_characters / total_words) - COLEMAN_LIAU_INDEX_CONSTANTS[
            'SECOND'] * (total_sentences / total_words)
        - COLEMAN_LIAU_INDEX_CONSTANTS['THIRD'])

    for readability_level, score in COLEMAN_LIAU_INDEX_LEVELS.items():
        if readability_score in score:
            readability_result = [readability_score, readability_level]

    return readability_result


def gunning_fog_index(total_words: float, total_complex_words: float, total_sentences: float) -> float:
    """
    Calculates readability score using the Gunning Fog Index.
    The Gunning Fog formula generates a grade level between 0 and 20. It estimates the education level
    required to understand the text.
    :param total_words: total amount of word in the text
    :param total_complex_words: total amount of complex words in the text
    :param total_sentences: total amount of sentences in the text
    :return: gunning fog index. The higher index the harder text readability is
    """

    readability_score = round(
        GUNNING_FOX_INDEX_CONSTANTS['FIRST'] * ((total_words / total_sentences) + (GUNNING_FOX_INDEX_CONSTANTS[
                                                                                       'SECOND'] * (
                                                                                               total_complex_words / total_words))))

    for readability_level, score in GUNNING_FOX_INDEX_LEVELS.items():
        if readability_score in score:
            readability_result = [readability_score, readability_level]

    return readability_result
