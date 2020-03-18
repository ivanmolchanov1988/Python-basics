# -*- coding: utf-8 -*-

'''
Создайте собственый класс-исключние, который должен проверять содержимое списка
на наличие только чисел.
Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных
элементов списка.

Длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта

'''

class MyError(Exception):
    def __init__(self):
        print('Это не число!')


oList = []

while True:
    a = input('введите число')
    if a == 'stop':
        print(oList)
        break
    try:
        a = int(a)
    except ValueError:
        MyError()
    else:
        oList.append(a)