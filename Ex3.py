# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

list = []
n = 10
for i in range(n):
    list.append(random.randint(1, 10))

def unique_numbers(list):
    result = []
    for char in list:
        if list.count(char) < 2:
            result.append(char)
    return result
 
print('Изначальный список: ', list)
print('Неповторяющиеся элементы из изначального списка: ', unique_numbers(list))