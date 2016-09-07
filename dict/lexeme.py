import pymorphy2

from pymorphy2 import *


inflect_word = "лабочка"

morph = pymorphy2.MorphAnalyzer()
info = morph.parse(inflect_word)[0]
j = 0
for i in info.lexeme:
    print(i,j)
    j = j + 1

