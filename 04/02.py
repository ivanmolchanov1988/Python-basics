# -*- coding: utf-8 -*-

'''Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента

Элементы, удовлетворяющие условию, оформить в виде списка.
Для оформления списка использовать генератор.
'''

from random import randrange

#oList = randrange(0, 100, 3)

oList = [randrange(0, 100, 3) for x in range(0, 25)]
print(oList)

oResult = [x for en, x in enumerate(oList) if x > oList[en - 1]]
print(oResult)