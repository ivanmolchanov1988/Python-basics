# -*- coding: utf-8 -*-

# Создать список и заполнить его элементами различных типов.

oList = [1, "1", 1., [1], {1}]

for i in oList:
    print(f"{i} - это {type(i)}")