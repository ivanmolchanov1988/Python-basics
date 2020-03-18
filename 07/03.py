# -*- coding: utf-8 -*-

''' 3. реализовать программу работы с органическими клетками
класс - клетка
параметры: целое число - кол-во клеток
должны быть перегрузки сложения add(), вычитания sub(), умножения mul(), деления truediv().

'''

class Kletka():
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        if self.n > other.n:
            return self.n - other.n
        else:
            return 'Ошибка!'

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        if self.n > other.n:
            return self.n // other.n
        else:
            return 'Ошибка!'

    def make_order(self, kol):
        oLine = ''
        oString = self.n // kol
        ost = self.n % kol
        for i in range(0, kol):
            for ii in range(0, oString):
                oLine += '*'
            print(oLine)
            oLine = ''
        print('*' * ost)

k1 = Kletka(60)
k2 = Kletka(7)
print(k1 + k2) # +
print(k2 - k1) # bad -
print(k1 - k2) # -
print(k1 * k2) # *
print(k1 / k2) # /
k2.make_order(3)
