# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

from random import randint 


def fill_list(n):
    f_list = []
    for i in range(n):
        f_list.append(randint(-n, n))
    return f_list

n = int(input("Введите число: "))
nums = fill_list(n)
print(nums)
positions = [1, 3, 6]
res = 1
for i in range(len(positions)):
    res *= nums[i]
    # print(nums[i])
print(res)
    

