# -*- coding: utf-8 -*-

'''
Реализовать класс Дата, принимает день-месяц-год.
1 метод: @classmethod, извлекает число, месяц, год и преобразовывет их в число.
2 метод: @staticmethod, должен проводить валидацию числа, месяца и года (месяц - от 1 до 12)

Я не уверен, что до конца понял всю суть задания.
'''

class Date:

    @classmethod
    def transform(cls, date):
        dList = ["первое", "второе", "третье", "четвёртое", "пятое"]
        mList = ["января", "февраля", "марта", "апреля", "мая"]
        yList = ["девятнадцатого", "двадцатого", "двадцать первого"]
        dmyList = [dList, mList, yList]
        template = str(date).split()
        result = ''
        for e, i in enumerate(template):
            for enum, ii in enumerate(dmyList[e]):
                if e == 0:
                    if i == ii:
                        result += f'0{enum + 1}.'
                if e == 1:
                    if i == ii:
                        result += f'0{enum + 1}.'
                if e == 2:
                    if i == ii:
                        result += f'{enum + 2019}'

        if Date.check(result) != False:
            print(result)

    @staticmethod
    def check(res):
        if len(str(res).split('.')) != 3:
            return False


q = Date()
q.transform('первое февраля девятнадцатого')