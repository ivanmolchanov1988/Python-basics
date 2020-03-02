# -*- coding: utf-8 -*-

'''Реализовать скрипт, в котором должна быть предусмотрена функция расчёта ЗП сотрудника
В расчёте необходимо использовать формулу:
(выработка в часах * ставка в час) + премия
Для выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами

'''

#Параметры: выработка в часах; ставка в час; премия

from sys import argv

def fZP(ofH, ofSt, ofPr):
    '''
    :param ofH: выработка в часах 
    :param ofSt: ставка в час
    :param ofPr: премия
    :return: oResult
    '''
    oResult = (ofH * ofSt) + ofPr
    return oResult

script_name, oH, oSt, oPr = argv
print(fZP(int(oH), int(oSt), int(oPr)))