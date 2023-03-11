# Задача №30. Заполните массив элементами арифметической прогрессии.

# a1 = int(input())
# d = int(input())
# n = int(input())
#
#
# def func(input_1, input_2, input_3):
#     an = input_1 + (input_3 - 1) * input_2
#     return an
#
#
# print(func(a1, d, n))

# Задача №32. Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума).

listMin = int(input('Введите минимальное значение массива: '))
listMax = int(input('Введите максимальное значение массива: '))
listOne = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def function(minel, maxel):
    for i in range(len(listOne)):
        if listMin <= listOne[i] <= listMax:
            print(i)


print(function(listMin, listMax))
