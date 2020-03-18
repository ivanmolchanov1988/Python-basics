# -*- coding: utf-8 -*-

'''
Создать собственный класс-исключение, обрабатывающий деление на ноль.
Проверить его на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя, программа должна корректно обрабатывать эту ситуацию
и не завершаться с ошибкой.
#ZeroDivisionError
'''

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt



a = input('введите первое число ')
b = input('введите второе число ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise MyError('Вы пытаетесь делить на ноль!')

except ValueError:
    print('Это не число')
except MyError:
    print(MyError('Вы пытаетесь делить на ноль!'))

else:
    print(a / b)