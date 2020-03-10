# -*- coding: utf-8 -*-

''' 2. Реализовать класс Road, в котором определить атрибуты length, width.
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчёта массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса для покрытия одного кв метра дороги, толщиной 1 см * число см толщины полотна.
Например: 20м * 5000м * 25кг * 5см = 12500т

'''

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self, onemetre = 25, depth = 5):
        omass = self._lenght * self._width * onemetre * depth
        return omass / 1000

oneRoad = Road(20, 5000)
print(str(oneRoad.mass()) + ' тонн')