import pymorphy2

# class Normalize():
#     def __init__(self,inflectWord):
#         self._inflect_word = inflectWord
#         self._normal_word = ""
#
#     def normalize(self):
#         morph = pymorphy2.MorphAnalyzer()
#         info = morph.parse(self._inflect_word)
#         self._normal_word = info[0][2]
#         print(self._normal_word)

class Word:
    def __init__(self, inputWord):
        self._input_word = inputWord
        self._normal_word = ""
        self._morph = pymorphy2.MorphAnalyzer()
        self.info = self._morph.parse(inputWord)[0].lexeme

    def normalize(self):
        info = self._morph.parse(self._input_word)
        self._normal_word = info[0][2]
        # print(self._normal_word)

    def getLexeme(self):
        for i in self.info:
            print(i.tag.case)


class Noun(Word):
    def __init__(self, inputWord):
        Word.__init__(self, inputWord)
        self._table_inflection = {}
        self._table = []
        self._cases = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']

    def fill_the_table(self):
        for i in self.info:
            if (str(i.tag.case)) in self._cases:
                self._table.append(i.word)
