# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            left = not (x or y or z )
            right = not x and not y and not z
            print(f'x= {x}, y= {y}, z={z}')
            print(left == right)


print('x y z \t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for n in range(64):
    n = bin(n)[2:].rjust(6, '0')
print(n)
# x, y, z = int(n[0]), int(n[1]), int(n[2])
# print(x, y, z, '\t', not(x or y or z) == (not(x) and not(y) and not(z)))