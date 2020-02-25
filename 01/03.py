# -*- coding: utf-8 -*-

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.

n = input('Введите число')
nn = n + n
nnn = n + n + n
result = int(n) + int(nn) + int(nnn)
print(result)
