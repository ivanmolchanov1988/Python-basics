# -*- coding: utf-8 -*-

'''Реализовать формирование списка
использую range()
и возможности генератора
в список должны войти чётные числа от 100 до 1000 включительно
Необходимо получить результат вычисления произведения всех элементов списка
использовать reduce()

'''

from functools import reduce

generator = [x for x in range(100, 1000 + 1) if x % 2 == 0]
print(generator)

def fff(one, two):
    return one * two

print(reduce(fff, generator))