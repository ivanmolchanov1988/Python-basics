# -*- coding: utf-8 -*-

'''
комплексные числа
перегрузка методов сложения и умножения

'''

class Dig():
    def __init__(self, dig):
        self.dig = dig

    def __add__(self, other):
        self.listDig = str(self.dig).split()
        self.listOther = str(other.dig).split()
        self.res = ''
        self.resOne = int(self.listDig[0][0]) + int(self.listOther[0][0])
        self.resTwo = int(self.listDig[2][0]) + int(self.listOther[2][0])
        if self.listDig[1] == '+':
            self.res = f'{self.resOne} + {self.resTwo}i'
        if self.listDig[1] == '-':
            self.res = f'{self.resOne} - {self.resTwo}i'
        return self.res


    def __mul__(self, other):
        self.listDig = str(self.dig).split()
        self.listOther = str(other.dig).split()
        self.res = ''
        self.resOne = int(self.listDig[0][0]) * int(self.listOther[0][0])
        self.resTwo = int(self.listDig[2][0]) * int(self.listOther[2][0])
        self.resThree = self.resOne - self.resTwo
        self.twoOne = int(self.listDig[0][0]) * int(self.listOther[2][0])
        self.twoTwo = int(self.listDig[2][0]) * int(self.listOther[0][0])
        self.resThree = self.twoOne + self.twoTwo
        if self.listDig[1] == '+':
            self.res = f'{self.resThree} + {self.resThree}i'
        if self.listDig[1] == '-':
            self.res = f'{self.resThree} - {self.resThree}i'
        return self.res




a1 = int(input('введите a: '))
b1 = int(input('введите b: '))
z1 = f'{a1} {"+" if b1 > 0 else "-"} {abs(b1)}i'
print(f'z1 = {z1}')
print(z1.split())

a2 = int(input('введите a: '))
b2 = int(input('введите b: '))
z2 = f'{a2} {"+" if b2 > 0 else "-"} {abs(b2)}i'
print(f'z1 = {z2}')

di1 = Dig(z1)
di2 = Dig(z2)
print()
print()
print(di1 + di2)
print(di1 * di2)
