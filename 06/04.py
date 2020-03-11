# -*- coding: utf-8 -*-

'''4. Реализуйте базовый класс Car. У данного класса должны быть атрибуты:
speed, color, name, is_police
и методы:
go, stop, turn(direction), который должны сообщать, что машина поехала, остановилась, повернула(куда)
Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar
переопределите метод show_speed.
При значении скорости выше 60(TownCar) и 40(WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экз классов. Передайте атрибуты. Выполните доступ к атрибутам, выведите результат.
Выпольните вызов методов и также покажите результат.

'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        self.oGo = False
    def go(self):
        self.oGo = True
        print(f'машина {self.name} поехала со скоростью ' + str(self.show_speed()) + ' км/ч')
    def stop(self):
        self.oGo = False
        print('машина не едет')
    def turn(self, direction):
        if self.oGo == False:
            print('мы не едем ')
        else:
            self.direction = direction
            print('мы повернули ' + str(self.direction))
    def show_speed(self):
        return self.speed

#bibi = Car(100, 'green', 'test', False)
#bibi.turn('вправо')
#bibi.go()
#bibi.turn('вправо')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
    def go(self):
        self.oGo = True
        print('машина поехала со скоростью ' + str(self.show_speed()) + ' км/ч')
        if self.speed > 60:
            print(f'{self.name} АСТАНАВИТЕС!')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
    def go(self):
        self.oGo = True
        print('машина поехала со скоростью ' + str(self.show_speed()) + ' км/ч')
        if self.speed > 40:
            print(f'{self.name} АСТАНАВИТЕС!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)

town = TownCar(100, 'red', 'bmw')
town.go()

work = WorkCar(45, 'green', 'ivanovez')
work.go()

police = PoliceCar(120, 'white', 'uaz')
police.go()

