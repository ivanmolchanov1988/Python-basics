# -*- coding: utf-8 -*-

'''Создать текстовый файл не программно
сохранить в нём несколько строк
выполнить посчёт кол-ва строк
и кол-ва слов в каждой строке

'''

with open('task02.txt') as oFile:
    for oEn, oLine in enumerate(oFile, 1):
        print(f'{oEn} {len(oLine.split())}: {oLine}')