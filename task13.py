import xml.etree.ElementTree as etree


class Wordform:
    def __init__(self, text, grams):
        self._text = text
        self._grams = grams

    def get_grams(self):
        return self._grams


class Sentence:
    def __init__(self, text, words):
        self._text = text
        self._words = words

    def get_text(self):
        return self._text

    def get_word(self, num):
        return self._words[num]

    def __len__(self):
        return len(self._words)


class Corpus:
    def __init__(self):
        self._sentences = []

    def get_sentence(self, num):
        return self._sentences[num]

    def load(self, filename):
        tree = etree.parse(filename)
        root = tree.getroot()
        for sent in root.iter('sentence'):
            text = sent.find('source').text
            words = []
            for token in sent.findall('tokens/token'):
                text = token.get('text')
                grams = []
                for gram in token.iter('g'):
                    grams.append(gram.attrib['v'])
                wordform = Wordform(text, grams)
                words.append(wordform)
            sentence = Sentence(text, words)
            self._sentences.append(sentence)
