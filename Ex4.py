# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import re
k = int(input('Введите степень k: '))

str_result = ''
for i in range(k + 1):
    kf = random.randint(0, 100)
    if i == 0:
        str_result = str(kf) + ' = 0'
    elif i == 1:
        if kf > 1:
            str_result = str(kf) + '*x + ' + str_result
        elif kf == 1:
            str_result = 'x + ' + str_result
    else:
        if kf > 1:
            str_result = str(kf) + '*x^' + str(i) + ' + ' + str_result
        elif kf == 1:
            str_result = 'x^' + str(i) + ' + ' + str_result

print(str_result)

data = open ('file1.txt', 'w')
data.write (str_result)
data.close()