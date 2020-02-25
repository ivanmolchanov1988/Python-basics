# -*- coding: utf-8 -*-

'''
Рейтинг
невозрастающий список натуральных чисел
Если в рейтинге существует этот элемент, то новый добавлять после них
'''

oList = []
oEll = ''
while True:
    oEll = input('Введите число или напишите "exit"')
    if oEll == 'exit':
        break
    if int(oEll) in oList:
        for i in enumerate(oList):
            if int(i[1]) == int(oEll):
                oList.insert(i[0], int(oEll))
                break
    elif len(oList) == 0 or int(oEll) < oList[len(oList)-1]:
        oList.append(int(oEll))
    elif int(oEll) > oList[0]:
        oList.insert(0, int(oEll))
    else:
        for ii, iii in enumerate(oList):
            if int(oEll) < iii and int(oEll) > oList[ii + 1]:
                print(iii, oList[ii + 1])
                oList.insert(ii + 1, int(oEll))
                break
    print(oList)