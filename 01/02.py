# -*- coding: utf-8 -*-
# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input('Введите секунды'))

import time     # для тестов

dsec = 0
hh = 3600
dhh = 0
mm = 60
dmm = 0

if sec % hh != False:
    dhh = sec // hh
    dsec = sec - hh * dhh
    if dsec % mm != False:
        dmm = dsec // mm
        dsec = dsec - mm * dmm
    else:
        dsec = int(dsec / mm)
else:
    dsec = int(sec / hh)

#print(f'0{dhh}') if dhh < 10 else print(f'{dhh}')
dhh = f'0{dhh}' if dhh < 10 else f'{dhh}'
dmm = f'0{dmm}' if dmm < 10 else f'{dmm}'
dsec = f'0{dsec}' if dsec < 10 else f'{dsec}'
print(f'{dhh}:{dmm}:{dsec}')

print(time.strftime('%H:%M:%S', time.gmtime(sec)))      # для тестов
