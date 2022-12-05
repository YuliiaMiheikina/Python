# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import randint


number = int(input('Введите длину списка '))
first_list = []
res_list = []

for i in range(number):
    first_list.append(randint(0, 10))

for i in range(len(first_list)):
    while i < len(first_list)/2 and number > len(first_list)/2:
        number = number - 1
        a = first_list[i] * first_list[number]
        res_list.append(a)
        i += 1

print(first_list)
print(res_list)