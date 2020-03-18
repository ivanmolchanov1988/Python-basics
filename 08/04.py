# -*- coding: utf-8 -*-

'''Начните над проектом "Склад техники". Создайте класс, описывающий склад.
А также класс "Оргтехника", который будет базовым для классов-наследников.
Эти классы - конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведённых типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Разраобтать методы, отвечающие за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и кол-ве единиц оргтехники, а также других данных,
можно исользовать любую подходящую структуру, например словарь.

Прошу прощения за оформление, тороплюсь сдать в срок
'''

class Storage():
    appDir = []     # список техники на складе
    appGive = []    # список выданной техники
    def __init__(self, name):
        # у склада есть имя\номер
        self.name = name

    def getIn(self, app, kol):
        # добавляет в список техники Наименование техники и её Кол-во
        self.appDir.append([app.name, kol])
        print(f'на склад добавлено {kol}шт: {app.name}')

    def giveOut(self, app, kol, podr):
        # если находит технику в списке имеющийся, вырезает оттуда нужное кол-во и вставляет в список
        # для выданной техники, добавляет наименование подразделения и наименование техники
        for i in self.appDir:
            if str(i[0]) == str(app.name):
                i[1] -= kol
                self.appGive.append([str(i[0]), kol, podr])
                print(f'отдали в {podr}: {str(i[0])} -- {kol} шт')

    def readIn(self):
        # построчно читает список имеющийся техники на ьекущем складе
        print('____________________________')
        for en, i in enumerate(self.appDir):
            print(f'{en+1}: {i[0]} -- {i[1]}шт')
        print('____________________________')

    def readOut(self):
        # построчно читает список выданной техники
        print('____________________________')
        for en, i in enumerate(self.appGive):
            print(f'{en+1}: {i[0]} -- {i[1]}шт, находится в {i[2]}')
        print('____________________________')



class Appliances():
    def __init__(self, name, width, height, length):
        self.name = name
        self.width = width
        self.height = height
        self.length = length


class Printer(Appliances):
    def __init__(self, name, width, height, length,
                 isMatrix = False, isSpray = False, isLazer = False):
        name = name + ' (Принтер)'
        super().__init__(name, width, height, length)
        self.isMatrix = isMatrix
        self.isSpray = isSpray
        self.isLazer = isLazer


class Scanner(Appliances):
    def __init__(self, name, width, height, length,
                 isTablet = False, isManual = False, isPlanetary = False):
        name = name + ' (Сканер)'
        super().__init__(name, width, height, length)
        self.isTablet = isTablet
        self.isManual = isManual
        self.isPlanetary = isPlanetary


class Xerox(Appliances):
    def __init__(self, name, width, height, length,
                 isSingle = False, isMultitool = False):
        name = name + ' (Ксерокс)'
        super().__init__(name, width, height, length)
        self.isSingle = isSingle
        self.isMultitool = isMultitool



x1 = Xerox('первый', 1, 2, 3, True)
storOne = Storage('первыйСклад')
storOne.getIn(x1, 10)
storOne.readIn()
p1 = Printer('один', 1, 1, 1, False, True)
storOne.getIn(p1, 6)
storOne.readIn()
storOne.giveOut(x1, 1, 'кадры')
storOne.giveOut(x1, 1, 'юристы')
storOne.readOut()
storOne.readIn()