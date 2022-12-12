# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите натуральное число: "))
muls = []

if num > 0:
    for i in range(2, num):
        while num% i == 0:
            muls.append(i)
            num//=i
    print(muls)
else:
    print("Введите число больше нуля!")
