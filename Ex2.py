# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math
n = int(input("Введите число: "))

def natural_numbers(n):
    list = []
    while n % 2 == 0:
        list.append(2),
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            list.append(i)
            n = n / i
    if n > 2:
        list.append(n)
    return list

print(natural_numbers(n))
