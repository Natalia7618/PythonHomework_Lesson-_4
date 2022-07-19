# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def get_random():
    return random.randint(0, 101)

def create_koef(k):
    lst = [get_random() for i in range(k+1)]
    return lst

def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

def get_stepen(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def get_member (member):
    member = member[0].replace(' ', '').split('=')
    member = member[0].split('+')
    list = []
    l = len(member)
    k = 0
    if get_stepen(member[-1]) == -1:
        list.append(int(member[-1]))
        l -= 1
        k = 1
    i = 1 
    ii = l - 1 
    while ii >= 0:
        if get_stepen(member[ii]) != -1 and get_stepen(member[ii]) == i:
            list.append(k_mn(member[ii]))
            ii -= 1
            i += 1
        else:
            list.append(0)
            i += 1
    return list

k1 = int(input("Введите степень для первого файла = "))
k2 = int(input("Введите степень для второго файла = "))
koef1 = create_koef(k1)
koef2 = create_koef(k2)
write_file("file2.txt", create_str(koef1))
write_file("file3.txt", create_str(koef2))    

with open('file2.txt', 'r') as data:
    member1 = data.readlines()
with open('file3.txt', 'r') as data:
    member2 = data.readlines()
print(f"Первый многочлен {member1}")
print(f"Второй многочлен {member2}")
list1 = get_member(member1)
list2 = get_member(member2)
ll = len(list1)
if len(list1) > len(list2):
    ll = len(list2)
lst_new = [list1[i] + list2[i] for i in range(ll)]
if len(list1) > len(list2):
    mm = len(list1)
    for i in range(ll,mm):
        lst_new.append(list1[i])
else:
    mm = len(list2)
    for i in range(ll,mm):
        lst_new.append(list2[i])
write_file("file4.txt", create_str(lst_new))
with open('file4.txt', 'r') as data:
    member3 = data.readlines()
print(f"Сумма многочленов =  {member3}")