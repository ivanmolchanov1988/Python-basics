# -*- coding: utf-8 -*-

'''Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

'''
from os import remove

oStr = '"Enter" - exit\n'
oInput = ''
while True:
    oInput = input(oStr)
    if oInput == '':
        break
    else:
        with open('task01.txt', 'a+') as oFile:
            oFile.write(oInput + '\n')

try:
    oFile = open('task01.txt')
    s = oFile.read()
    print(s)
    oFile.close()
    remove('task01.txt')
except FileNotFoundError:
    print('Вы ничего не написали')