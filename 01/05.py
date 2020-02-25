# -*- coding: utf-8 -*-

# Запросите у пользователя значение выручки и издержки фирмы
# Прибыль или выручка?
# Если с прибылью, то с какой?
# После запросить кол-во сотрудиклв и определить прибыль для каждого

profit = int(input('Profit'))
#profit = 800
loss = int(input('Loss'))
#loss = 700
if profit > loss:
    net_prof = profit - loss
    print(net_prof, '-- Net profit')
    empl = int(input('Ho many employees do you have?'))
    print(net_prof / empl, '-- profit for one employee')
