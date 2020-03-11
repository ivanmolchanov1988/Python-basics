# -*- coding: utf-8 -*-

''' 3. реализовать базовый класс Worker, в котором определить атрибуты: name, surname, position, income.
Последний атрибут защищённый и ссылается на словарь, содержащий элементы: оклад и премия ({'wage': wage, 'bonus': bonus})
Создать класс Position на базе класса Worker. Реализовать методы получения полного имени сотрудника get_full_name и
дохода с учётом премии get_total_income
Проверить работу примера на реальных данных

'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        income = {'wage': self.wage, 'bonus': self.bonus}
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        fullName = self.name + ' ' + self.surname
        return fullName
    def get_total_income(self):
        total = self.wage + self.bonus
        return total

petya = Position('Petya', 'Petrov', 'programmer', 70000, 30000)
print(petya.get_full_name())
print(petya.get_total_income())

# Не понял смысл словаря. Или я что-то не так делаю, или очень странная логика наследования.