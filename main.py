# Задача №30. Заполните массив элементами арифметической прогрессии.

a1 = int(input())
d = int(input())
n = int(input())


def func(input_1, input_2, input_3):
    an = input_1 + (input_3 - 1) * input_2
    return an


print(func(a1, d, n))