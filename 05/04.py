# -*- coding: utf-8 -*-

'''Создать непрограммно файл
One - 1
Two - 2
Three - 3
Four - 4

Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

'''
oDict = {'One': 'Одни', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('task04w.txt', 'w') as oFileExport:
    with open('task04.txt') as oFileImport:
        for oLine in oFileImport:
            try:
                oResult = list(x for x in oLine.split()[1:])
                oResult.insert(0, oDict[oLine.split()[0]])
                oFileExport.write(' '.join(oResult) + '\n')
            except:
                oFileExport.write(oLine)

with open('task04w.txt') as oFileExport:
    print(oFileExport.read())