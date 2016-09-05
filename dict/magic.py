import pymorphy2

class Word:
    def __init__(self, inputWord):
        self._input_word = inputWord
        self._normal_word = ""
        self._morph = pymorphy2.MorphAnalyzer()
        self.info = self._morph.parse(inputWord)[0].lexeme
        self._pos = self._morph.parse(inputWord)[0].tag.POS

    def normalize(self):
        info = self._morph.parse(self._input_word)
        self._normal_word = info[0][2]
        # print(self._normal_word)

class Noun(Word):
    def __init__(self, inputWord):
        Word.__init__(self, inputWord)
        self._inflected_words = []
        self._singular = []
        self._plural = []
        self._context = {}
        self._cases = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']
    def lookup_words(self):
        for i in self.info:
            if (str(i.tag.case)) in self._cases:
                self._inflected_words.append(i.word)
    def detach_words(self):
        for i in range(0, 6):
            self._singular.append(self._inflected_words[i])
            self._plural.append(self._inflected_words[i+6])
        self._context = zip(self._singular,self._plural)



noun = Noun('лампочка')

noun.lookup_words()

print(noun._inflected_words)

# print (noun._table_inflection)
