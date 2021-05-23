from nltk import sent_tokenize, word_tokenize, pos_tag


def text_parser(raw_text: str) -> dict:
    """
    Transforms raw text into sentence and word tokens, tags them.
    :param raw_text: raw text from input file
    :return: a dictionary of raw text word, sentence tokens and tags.
    """
    word_token = []

    sent_token = sent_tokenize(raw_text)
    for x in sent_token:
        word_token += word_tokenize(x)

    tagged = pos_tag(word_token)

    return dict(
        raw_text=raw_text,
        word_token=word_token,
        sentence_token=sent_token,
        tagged=tagged
    )
