import unittest
import os
from task13 import Corpus


class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.corpus = Corpus()
        self.corpus.load(('annot.opcorpora.no_ambig.xml'))

    def test_corpus_len(self):
        self.assertIsNotNone(self.corpus)

    def test_sentence_len(self):
        sentence = self.corpus.get_sentence(0)
        self.assertEqual(len(sentence), 7)

if __name__ == '__main__':
    unittest.main()