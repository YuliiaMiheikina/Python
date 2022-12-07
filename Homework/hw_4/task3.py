# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


n = int(input("Введите длину списка: "))

numbers = []
for i in range(n):
    numbers.append(randint(1,10))
print(numbers)



new_lst = []
for i in numbers:
    if numbers.count(i) < 2:
        new_lst.append(i)
print(new_lst)