# -*- coding: utf-8 -*-

'''реализовать функцию init_func()
принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой

'''

def init_func(oInitStr):
    result = ''
    for i, oSimbol in enumerate(oInitStr):
        if i == 0:
            result += oSimbol.upper()
        else:
            result += oSimbol.lower()
    return result

print(init_func('qwerty'))
