# -*- coding: utf-8 -*-

'''реализовать функцию my_func(),
которая принимает три позиционных аргумента
 и возвращает сумму наибольших двух аргументов.

'''

def my_func(a, b, c):
    '''
    :param a: первое число
    :param b: второе число
    :param c: третье число
    :return: сумма двух самых больших числа
    '''
    oList = [a, b, c]
    z = max(oList)
    oList.remove(z)
    x = max(oList)
    return z + x


print(my_func(1, 2, 3))
