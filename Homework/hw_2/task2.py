# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
number = int(input("Введите число N: "))
factorial = 1
numbers = []
for i in range(1, number+1):
    factorial *= i
    # print(factorial, end=",")
    numbers.append(factorial)
print(numbers)
print(*numbers, sep=" ")