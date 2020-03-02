# -*- coding: utf-8 -*-


'''
Реализовать два небольших скрипта
1 - бесконечный итераторб генерирующий целые числа, начиная с указанного
2 - бесконечный итератор, повторяющий элементы некоторого списка, определённого заранее

Использовать функцию count() & cycle() from itrtools
'''

from itertools import count, cycle as board

endboard = 0
write = 'I will not skateboard in the halls '
for bart in board(write):
    if endboard >= len(write) * 50:
        break
    else:
        print(bart)
        endboard += 1


for i in count(15):
    if i > 17:
        break
    else:
        print(i, 'using the count')
