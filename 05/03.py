# -*- coding: utf-8 -*-

'''Создать текстовый файл не программно
построчно записать фамилии сотрудников и величину их окладов
Определить, кто из сотрудников имеет оклад меньше 20 тыс
вывести фамилии этих
Выпольнить подсчёт средней величины дохода сотрудников

'''

with open('task03.txt') as oFile:
    oAll = 0
    oColl = 0
    oBadnews = []
    for oEn, oLine in enumerate(oFile, 1):
        oColl = oEn
        zp = int(oLine.split()[1])
        oEmpl = oLine.split()[0]
        oAll += zp
        if zp < 20000:
            oBadnews.append(oEmpl)
    print(f'Им нужно повысить ЗП: {oBadnews}')
    print(f'А в среднем такие дела - {oAll / oColl}')

print('\n\n', open('task03.txt').read())
open('task03.txt').close()