# -*- coding: utf-8 -*-

# Пользователь вводит целое число
# Найдите самую большую цифру в числе.

n = input('Введите число')
#n = str(898)
i = 0
ii = 0
temp = ''
result = 0
while i <= int(n[ii]):
    if i == int(n[ii]):
        temp = temp + n[ii]
        if int(n[ii]) > result:
            result = int(n[ii])
        i = 0
        ii = ii + 1
    i = i + 1
    if temp == n:
        break
print(result, '-- самая большая цифра из введённого Вами числа')
