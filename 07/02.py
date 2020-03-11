# -*- coding: utf-8 -*-

''' 2. Реализовать проект суммарного расхода ткани на производство одежды.
Основная сущность-кслаас - одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер(для пальто) и рост(для костюма).
Это могут быть обычные числа V and H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто -- V / 6.5 + 0.5
для костюма -- 2 * H + 0.3

реализовать общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property

'''
from abc import ABC, abstractmethod

class Odejda(ABC):
    def __init__(self, param, oNext = 0):
        self.param = param
        self.onext = oNext

# Тут я совсем не понимаю, почему ругается, если раскомментировать @abstractmethod :(
#   @abstractmethod
    def met(self):
        pass

    @property
    def suum(self):
        a = self.param / 6.5 + 0.5
        b = self.onext * 2 + 0.3
        return a + b

class V(Odejda):
    def met(self):
        return self.param / 6.5 + 0.5

class H(Odejda):
    def met(self):
        return self.param * 2 + 0.3


v = V(5)
print(v.met())

h = H(5)
print(h.met())

o = Odejda(5,5)
print(o.suum)