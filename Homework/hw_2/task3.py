# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Для n = 6:
#     [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#     Сумма чисел = 14.0717
n = int((input("Введите число n: ")))
summ = 0
nums = []
for i in range(1,n+1):
    res = round(((1 +1/i)**i), 2)
    nums.append(res)
    summ =  summ + res
print(nums)
print(summ)



# print(sum(nums))
# print(max(nums))
# print(min(nums))