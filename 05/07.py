# -*- coding: utf-8 -*-

'''Создать непрограммно текстовый файл, в котором каждая строка должна содежать данные о фирме:
название, форма собственности, выручка, издержки
firm_1 ООО 10000 500.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью
Если фирма получила убытки, также добавить ее в словарь со значением убытков.
[{'firm_1': 5000, 'firm_2': 3000, 'firm_3': 1000}, {'average_profit': 2000}].
Итоговый список сохранить в json

(менеджеры контекста)

'''
with open('task07.txt') as oFile:
    print(oFile.read())


with open('task07.txt') as oFile:
    import json
    oList = []
    oDirFIrms = {}
    oCol = 0
    oDirMean = {}
    oDirMean['mean profit'] = 0
    for q, oLine in enumerate(oFile, 1):
        oKey = ''
        for en, i in enumerate(oLine.split()):
            if en == 0:
                oDirFIrms[i] = 0
                oKey = i
            if en == 2:
                oDirFIrms[oKey] += int(i)
            if en == 3:
                oDirFIrms[oKey] -= int(i)
                if oDirFIrms[oKey] > 0:
                    oCol += 1
                    oDirMean['mean profit'] += oDirFIrms[oKey]

    print(oDirFIrms)
    print(oCol)
    oDirMean['mean profit'] = oDirMean['mean profit'] / oCol
    print(oDirMean['mean profit'])
    oList.append(oDirFIrms)
    oList.append(oDirMean)
    print(oList)

    with open('task07jsn.txt', 'w') as oJsn:
        oJsn.write(json.dumps(oList, ensure_ascii=False))

    with open('task07jsn.txt') as oJsn:
        print('\nin file --- ' + oJsn.read())