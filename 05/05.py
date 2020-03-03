# -*- coding: utf-8 -*-

'''Создать программно текстовый файл
записать в него программно набор чисел, разделённых пробелами
Программа должна подсчитать сумму чисел в файле и вывести её на экран

'''

with open('task05.txt', 'w') as oFile:
    from random import randint
    oCol = randint(5, 5 * 5)
    oStr = ''
    oSum = 0
    for i in range(1, oCol):
        oStr += str(i) + ' '
        oSum += i
    oFile.write(oStr)
    print(oSum)

with open('task05.txt') as oFile:
    oList = oFile.read().split()
    print(oList)
    oSum = 0
    for i in oList:
        oSum += int(i)
    print(oSum)