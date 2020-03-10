# -*- coding: utf-8 -*-

'''5. Реализовать класс Stationery канцелярская принадлежность. Определить в нём атрибут title  название
и метод draw отрисовка. Метод выводит сообщение - запуск отрисовки.
Создать три дочерних класса Pen, pencil, Handle.
В каждом из классов реализовать метод draw. Для каждого из классов выводить из метода уникальные сообщения.

'''

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки!')

class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)
    def draw(self):
        print(f'Запуск отрисовки для РУЧКИ!')

class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)
    def draw(self):
        print(f'Запуск отрисовки для карандашика!')

class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)
    def draw(self):
        print(f'Запуск отрисовки для Маркера!')

ru = Handle('Ручка')
ru.draw()