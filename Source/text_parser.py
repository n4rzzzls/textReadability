from nltk import sent_tokenize, word_tokenize, pos_tag


# Transforms raw text into sentence and word tokens; tags them.
# Returns a dictionary of raw text word, sentence tokens and tags.
def text_parser(raw_text):
    """

    :param raw_text:
    :return:
    """
    word_token = []

    sent_token = sent_tokenize(raw_text)
    for x in sent_token:
        word_token += word_tokenize(x)

    tagged = pos_tag(word_token)

    return dict(
        rawText=raw_text,
        wordToken=word_token,
        sentToken=sent_token,
        tagged=tagged
    )
