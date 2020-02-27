# -*- coding: utf-8 -*-

'''Программа запрашивает у пользователя строку чисел, разделённых пробелом
При нажатии ENTER должна выводиться сумма чисел
Пользователь может продолжить ввод чисел и т.д.
Сумма новых чисел будет прибавляться к старой
Спец символ - выход
Если спеиальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее и после этого завершить

'''

def fInput(ofInputString):
    ofInputOutStr = []
    for i in ofInputString.split():
        try:
            i = int(i)
            ofInputOutStr.append(i)
        except ValueError:
            if i == 'exit':
                return [sum(ofInputOutStr), 'exit']
                #pass #!!!
            else:
                #print('Только числа и пробелы!')
                return
    return sum(ofInputOutStr)


oExit = 'noExit'
oOut = 0
while oExit != 'exit':
    oString = input('пиши строку сюда (выход-"exit") --- ')
    oResult = fInput(oString)
    if type(oResult) != type([]):
        try:
            oOut += oResult
            print(oOut)
        except TypeError:
            print('Только числа и пробелы!')
            oExit = 'exit'
    else:
        oOut += oResult[0]
        print(oOut)
        oExit = 'exit'