# -*- coding: utf-8 -*-

# Каждый день бегает
# 1 - а км
# а = а + 10% а
# через сколько дней будет б км?

a = int(input('Начало'))
#a = 5
a = a - a * 0.1
#b = 50
b = int(input('Конец'))
i = 0
while b > a:
    i += 1
    a = a + a * 0.1
    print(f'день{i}: {a}')