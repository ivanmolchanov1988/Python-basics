# -*- coding: utf-8 -*-

'''Необходимо сздать непрограммно текстовый файл
где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных и их кол-во
Важно, чтобы для каждого предмета не обязательно были все типы занятий

Сформировать словарь, который содеожит название предмета и общее кол-во занятий по нему.
Вывести словарь на экран

'''

with open('task06.txt') as oFile:
    print(oFile.read())


with open('task06.txt') as oFile:
    oDir = {}
    for oLine in oFile:
        #oDir[oLine.split().pop(0)] =
        oKey = ''
        for en, oStr in enumerate(oLine.split()):
            if en == 0:
                oDir[oStr[:-1]] = 0
                oKey = oStr[:-1]
            else:
                try:
                    i = oStr.find('(')
                    oInt = int(oStr[:i])
                    oDir[oKey] += oInt
                except:
                    pass

    print(oDir)