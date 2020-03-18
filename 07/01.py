# -*- coding: utf-8 -*-

''' 1. Реализовать класс Matrix. Обеспечить перегрузку конструктора класса (метод inti()), который должен
принимать данные (список списков) для формирования матриы.
Следующий шаг - реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатов сложения должна быть новая матрица.
Полсказка: сложение элементов матриц выполнять поэлементно -
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

'''


class Matrix:
    def __init__(self, *agrs):
        #import numpy as np
        self.mtrx = []
        for i in agrs:
            self.mtrx.append(i)
        #print(self.mtrx)        #-- проверка, всё хорошо.
    def __str__(self):
        oStr = ''
        oN = '\n'
        for i in self.mtrx:
            for en, ii in enumerate(i):
                oStr += ' ' +str(ii)
                if en == len(i)-1:
                    oStr += oN
        return (oStr)
    def __add__(self, other):
        import numpy as np
        left = np.array(self.mtrx)
        right = np.array(other.mtrx)
        oSum = left + right
        return oSum

m = Matrix([1,2,1],[3,4,1],[5,6,1],[7,1,8])
print(m)
b = Matrix([1,1,1],[1,1,1],[1,1,1],[1,1,1])
print(m + b)