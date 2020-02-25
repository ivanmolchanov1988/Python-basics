# -*- coding: utf-8 -*-

# Для списка реализовать обмен значений соседних элементов.
oExit = ''
oList = []
while oExit != "exit":
    oExit = input("Введите число или 'exit' для выхода")
    if len(oList) % 2 == 0 or len(oList) == 0:
        oList.append(oExit)
    elif len(oList) % 2 != 0:
        oList.append(oList[len(oList) - 1])
        oList[len(oList) - 2] = oExit

    print(oList)