# -*- coding: utf-8 -*-


'''реализовать генератор с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
функция должна вызываться следующим образом:
for el in fibo_gen()

Функция отвечает за получение факториала числв, а в цикле необходимо выводить только
первые 15 чисел.

'''

def fibo_gen(n):
    temp = 1
    for i in range(1, n):
        yield i * temp
        temp *= i

f = fibo_gen(150)

for el, i in enumerate(f, 1):
    if el >= 15:
        break
    else:
        print(el, i)
