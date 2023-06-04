import unittest
import json
from task14 import TFIDF


class TestTFIDF(unittest.TestCase):

    def setUp(self):
        self.object = TFIDF(['1.txt', '2.txt'])
        self.tfidf = self.object.count_tfidf('3.txt')

        with open('idfs.json', 'r', encoding='utf-8') as f:
            self.idfs = json.load(f)

    def test_texts(self):
        self.assertIsNotNone(self.object.get_texts())

    def test_idfs(self):
        for word in self.idfs:
            with self.subTest(word=word):
                self.assertEqual(self.idfs[word], self.object.get_idfs()[word])


if __name__ == '__main__':
    unittest.main()