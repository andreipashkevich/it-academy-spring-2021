"""Homework 4 - Task7

Оглянемся назад. Числа
Даны два натуральных числа. Вычислите их наибольший общий делитель
при помощи алгоритма Евклида (мы не знаем функции и рекурсию).
"""

a = 248
b = 12

while a and b:
    if a > b:
        a %= b
    else:
        b %= a
print(a + b)
