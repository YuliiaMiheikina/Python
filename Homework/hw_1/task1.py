# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
d = int(input("Введите номер дня недели: "))
if 1 <= d <= 7:
    if d > 5:
        print("Weekend!")
    else:
        print("Working day!")
else:
    print("Нет такого дня недели!")