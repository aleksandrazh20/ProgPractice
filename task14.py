import json
import math
import os
from collections import Counter
import pymorphy2


class TFIDF:

    def __init__(self, files: list):
        self._texts = []
        self._idfs = {}
        self._morph = pymorphy2.MorphAnalyzer()
        for file in files:
            self._texts.append(self._add_file(file)[1])
        if os.path.exists("idf.json"):
            with open('idf.json', 'r', encoding='UTF-8') as f:
                self._idfs = json.load(f)
        else:
            for text in self._texts:
                self._count_idf(text)

    def _add_file(self, item):
        with open(item, "r", encoding='UTF-8') as d:
            text = d.read()
        for symbol in '.,;:""?!-0123456789()—–«»':
            text = text.replace(symbol, '')
        w = text.lower().split()
        words = [self._morph.parse(word)[0].normal_form for word in w]
        w_count = Counter(words)
        return words, w_count

    def get_idfs(self):
        return self._idfs

    def get_texts(self):
        return self._texts

    def _count_idf(self, texts):
        for word in texts:
            d = len(self._texts)
            num = 0
            for texts in self._texts:
                if word in texts:
                    num += 1
            self._idfs[word] = math.log(abs(d) / abs(num))
        with open('idf.json', 'w', encoding="utf-8") as d:
            json.dump(self._idfs, d, ensure_ascii=False, indent=4)

    def count_tfidf(self, file):
        words, word_count = self._add_file(file)
        tfidfs = []
        l = len(words)
        for word in word_count:
            tf = word_count[word] / l
            idf = self._idfs.get(word, 0)
            tfidfs.append((word, tf * idf))
        return tfidfs