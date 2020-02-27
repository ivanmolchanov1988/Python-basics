# -*- coding: utf-8 -*-

# Пользователь вводит месяц елым числом от 1 до 12
# Какое это время года?
# использовать list and dict

# list
oList = [['winter',[1, 2, 12]], ['spring',[3, 4, 5]], ['summer',[6, 7, 8]], ['autumn',[9, 10, 11]]]
mm = int(input("Введите число от 1 до 12"))

for i in oList:
    for ii in i[1]:
        if ii == mm:
            print(i[0])

# dict
oDict = {'Winter':[1,2,12], 'Spring':[3,4,5], 'summer':[6,7,8], 'Sutumn':[9,10,11]}

for i in oDict.items():
    for ii in i[1]:
        if ii == mm:
            print(i[0])