# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

import math

from random import uniform


n = int(input('Введите длину списка:'))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))
print(list1)

list2 = []
for i in range(len(list1)):
    rem = round(list1[i] % 1, 2)
    list2.append(rem)
print(list2)

max_rem = max(list2)
min_rem = min(list2)

dif = round((max_rem - min_rem), 2)
print(max_rem, min_rem)
print(dif)



