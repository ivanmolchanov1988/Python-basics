# -*- coding: utf-8 -*-
'''
Пользователь вводит строку из нескольких слов
вывести каждое слово с новой строки
строки пронумеровать
слово выводить до 10го (включительно) символа
'''

oString = input('Напишите что-нибудь')
ii = 1
for i in oString.split():
    if len(i) > 10:
        print(ii, i[:10])
    else:
        print(ii, i)
    ii += 1