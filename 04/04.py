# -*- coding: utf-8 -*-

'''Представлен списокчисел
Определить элементы списка, не имеющие повторений
Сформировать итоговый массив чисел
соответствующий требованию.
Элементы вывести в порядке их следования в исхоном списке.
Использовать генератор

'''

from random import randrange

#oList = randrange(0, 100, 3)

oList = [randrange(0, 100, 3) for x in range(0, 25)]
print(oList)

oResult = [x for x in oList if oList.count(x) == 1 ]
print(oResult)