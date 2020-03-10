# -*- coding: utf-8 -*-

''' 1. Создать класс TrafficLight и определить у него один атрибут color и метод running. Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зелёный. Продолжительность красного - 7сек
желтого - 2сек, зелёного - как получится.

'''

import time

class TrafficLight:
    def __init__(self, color, otime = 5):
        self._color = color
        self._tempColor = None
        self.time = otime

    def runnig(self):
        while True:
            if self._color == 'red':
                print('RED')
                time.sleep(7)
                self._color = input('переключить на жёлтый? (y / n)')
                if self._color == 'y':
                    self._color = 'yellow'
                elif self._color == 'n':
                    self._color = 'red'
            elif self._color == 'yellow':
                print('YELLOW')
                time.sleep(2)
                self._color = input('на какой цвет переключить? (r / g)')
                if self._color == 'r':
                    self._color = 'red'
                elif self._color == 'g':
                    self._color = 'green'
            elif self._color == 'green':
                print('GREEN')
                time.sleep(self.time)
                self._color = input('переключить на жёлтый? (y / n)')
                if self._color == 'y':
                    self._color = 'yellow'
                elif self._color == 'n':
                    self._color = 'green'
            else:
                print('Вы сломали светофор!')
                break

svet = TrafficLight('red')
svet.runnig()

# Я не очень понял суть задания, если честно.
# Кажется, что сделал что-то не то :/