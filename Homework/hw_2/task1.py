# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.


# number = float(input("Введите вещественное число: "))
# sum = 0

# while (number != int(number)):
#     number = number * 10
# while (number != 0):
#     sum = sum + number % 10
#     number = number //10
# print(sum)


num = input("Введите вещественное число: ")

# x = num.split(".") 
# a = int(x[0]) 
# b = int(x[1]) 
# sum = 0
# while (a != 0): 
#     sum = sum + (a % 10)
#     a = a // 10
# while (b != 0): 
#     sum = sum + (b % 10)
#     b = b // 10
# print("Сумма цифр равно:", sum)
res = 0
for i in num:
    if i.isdigit():
        res += int(i)
print(res)
