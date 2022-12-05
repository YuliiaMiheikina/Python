# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

n = int((input("Введите число n: ")))
nums = []
summ = 0
for i in range(n):
    nums.append(randint(1,20))
print(nums)

for i in range(1, len(nums)+1, 2) :
      summ += nums[i - 1]
print(summ)

    

