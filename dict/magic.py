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
        self._case1 = {}
        self._case1['explaination'] = 'Кто? Что?'
        self._case1['example'] = 'хомяк ест'
        self._case2 = {}
        self._case2['explaination'] = 'Кого? Чего?'
        self._case2['example'] = 'у нас нет хомяка'
        self._case3 = {}
        self._case3['explaination'] = 'Кому? Чему?'
        self._case3['example'] = 'сказать хомяку спасибо'
        self._case4 = {}
        self._case4['explaination'] = 'Кого? Что?'
        self._case4['example'] = 'хомяк читает книгу'
        self._case5 = {}
        self._case5['explaination'] = 'Кем? Чем?'
        self._case5['example'] = 'зерно съедено хомяком'
        self._case6 = {}
        self._case6['explaination'] = 'О ком? О чём? '
        self._case6['example'] = 'хомяка несут в корзинке'
        # self._inflected_words = []
        self._context = []
    def lookup_words(self):
        for i in self.info:
            if (str(i.tag.case) == 'nomn'):
                if ('sing' in str(i.tag.number )):
                    self._case1['sing'] = i.word
                else:
                    self._case1['plur'] = i.word

            elif (str(i.tag.case) == 'gent'):
                if ('sing' in str(i.tag.number)):
                    self._case2['sing'] = i.word
                else:
                    self._case2['plur'] = i.word

            elif (str(i.tag.case) == 'datv'):
                if ('sing' in str(i.tag.number )):
                    self._case3['sing'] = i.word
                else:
                    self._case3['plur'] = i.word

            elif (str(i.tag.case) == 'accs'):
                if ('sing' in str(i.tag.number )):
                    self._case4['sing'] = i.word
                else:
                    self._case4['plur'] = i.word

            elif (str(i.tag.case) == 'ablt'):
                if ('sing' in str(i.tag.number )):
                    self._case5['sing'] = i.word
                else:
                    self._case5['plur'] = i.word

            elif (str(i.tag.case) == 'loct'):
                if ('sing' in str(i.tag.number )):
                    self._case6['sing'] = i.word
                else:
                    self._case6['plur'] = i.word

        for i in (self._case1,self._case2,self._case3,self._case4,self._case5,self._case6):
            self._context.append(i)
        # def detach_words(self):
        # for i in range(0, 6):
        #     self._singular.append(self._inflected_words[i])
        #     self._plural.append(self._inflected_words[i+6])
        # self._context = zip(self._singular,self._plural)



noun = Noun('ты')

noun.lookup_words()

print(noun._context)



# print (noun._table_inflection)
