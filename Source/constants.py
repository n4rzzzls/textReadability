COMPLEX_WORD_SYLLABLES = 3
LONG_WORD_SYLLABLES = 7

KINCAID_GRADE_LEVEL_CONSTANTS = dict(FIRST=0.39,
                                     SECOND=11.8,
                                     THIRD=15.59)

FLESH_READING_EASE_CONSTANTS = dict(FIRST=206.835,
                                    SECOND=1.015,
                                    THIRD=84.6)
ARI_CONSTANTS = dict(FIRST=4.71,
                     SECOND=0.5,
                     THIRD=21.43)

COLEMAN_LIAU_INDEX_CONSTANTS = dict(FIRST=5.879851,
                                    SECOND=29.587280,
                                    THIRD=15.800804)

GUNNING_FOX_INDEX_CONSTANTS = dict(FIRST=0.4,
                                   SECOND=100)

KINCAID_GRADE_LEVELS = {
    'Basic level': range(0, 1, 1),
    'Easy to read': range(1, 5, 1),
    'Average difficulty': range(5, 11, 1),
    'The text is for skilled readers': range(11, 19, 1)
}


FLESH_READING_EASE_LEVELS = {
    'Extremely difficult to read. Best understood by university graduates': range(0, 10, 1),
    'Very difficult to read. Best understood by university graduates': range(10, 30, 1),
    'Difficult to read': range(30, 50, 1),
    'Fairly difficult to read': range(50, 60, 1),
    'Plain English. Easily understood by 13- to 15-year-old students': range(60, 70, 1),
    'Fairly easy to read': range(70, 80, 1),
    'Easy to read. Conversational English for consumers': range(80, 90, 1),
    'Very easy to read. Easily understood by an average 11-year-old student': range(90, 100, 1)
}

ARI_LEVELS = {
    'Basic level': range(0, 1, 1),
    'Very easy to read': range(1, 5, 1),
    'A text is considered ideal for average readers': range(5, 8, 1),
    'Fairly difficult to read': range(8, 11, 1),
    'Too hard to read for the majority of readers': range(10, 20, 1)
}


COLEMAN_LIAU_INDEX_LEVELS = {
    'Basic level': range(0, 1, 1),
    'Very easy to read': range(1, 5, 1),
    'A text is considered ideal for average readers': range(5, 8, 1),
    'Fairly difficult to read': range(8, 11, 1),
    'Too hard to read for the majority of readers': range(10, 20, 1)
}


GUNNING_FOG_INDEX_LEVELS = {
    'Basic level': range(0, 1, 1),
    'Very easy to read': range(1, 5, 1),
    'A text is considered ideal for average readers': range(5, 8, 1),
    'Fairly difficult to read': range(8, 11, 1),
    'Too hard to read for the majority of readers': range(11, 21, 1)
}


GRADES_RANGE = {
    'kincaid': 19,
    'flesch': 100,
    'ari': 20,
    'coleman': 20,
    'fog': 21
}
