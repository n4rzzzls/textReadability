import sys
sys.path.append("../source")
import unittest
from source import text_stats as ts


class TestTextStats(unittest.TestCase):

    def test_words_count(self):

        text = ['Two', 'hundred', 'Palestinians', 'including', 'children']

        result = ts.get_words_count(text)

        self.assertEqual(result, 5)

    def test_sentences_count(self):

        sentences = ['Two hundred Palestinians, including 59 children', 'have been killed during a week of attacks in Gaza',
                     'Early on Monday, warplanes launched more heavy airstrikes on Gaza City']

        result = ts.get_sentence_count(sentences)

        self.assertEqual(result, 3)

    def test_syllables_count(self):

        word1 = "thought"
        word2 = "early"
        word3 = "including"

        result1 = ts.get_syllables_counter(word1)
        result2 = ts.get_syllables_counter(word2)
        result3 = ts.get_syllables_counter(word3)

        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 3)

    def test_chars_count(self):

        word = ["readability", "text"]

        result = ts.get_characters_count(word)

        self.assertEqual(result, 15)

    def test_words_filter(self):

        sentence = [('Two', 'CD'), ('hundred', 'CD'), ('Palestinians', 'NNPS'), (',', ','), ('including', 'VBG'),
                    ('59', 'CD'), ('children', 'NNS'), (',', ','), ('have', 'VBP'), ('been', 'VBN'), ('killed',
                    'VBN'), ('during', 'IN'), ('a', 'DT'), ('week', 'NN'), ('of', 'IN'), ('attacks', 'NNS'),
                    ('in', 'IN'), ('Gaza', 'NNP'), (',', ','), ('health', 'NN'), ('officials', 'NNS'), ('in', 'IN'), (
                    'the', 'DT'), ('territory', 'NN'), ('have', 'VBP'), ('said', 'VBD'), (',', ','), ('as', 'IN'),
                    ('Benjamin', 'NNP'), ('Netanyahu', 'NNP'), ('signalled', 'VBD'), ('Israel', 'NNP'), ("'s", 'POS'),
                    ('bombardment', 'NN'), ('would', 'MD'), ('rage', 'VB'), ('on', 'IN'), ('despite', 'IN'),
                    ('mounting', 'VBG'), ('global', 'JJ'), ('pressure', 'NN'), ('to', 'TO'), ('stop', 'VB'),
                    ('the', 'DT'), ('bloodshed', 'NN'), ('.', '.')]

        expected = ['Two', 'hundred', 'Palestinians', 'including', 'children', 'have', 'been', 'killed', 'during',
                    'a', 'week', 'of', 'attacks', 'in', 'Gaza', 'health', 'officials', 'in', 'the', 'territory',
                    'have', 'said', 'as', 'Benjamin', 'Netanyahu', 'signalled', "Israel's", 'bombardment', 'would',
                    'rage', 'on', 'despite', 'mounting', 'global', 'pressure', 'to', 'stop', 'the', 'bloodshed']

        result = ts.word_token_filter(sentence)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
