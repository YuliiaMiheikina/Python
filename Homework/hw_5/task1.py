# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("text.txt", "w", encoding = 'utf-8') as f:
    f.write("Умениеабв создавать файлыабв в Python открывает массу новых возможностейабв — например,\nпозволяет хранить данные, сохраняя их согласованность для разных пользователей.\n")

with open('text.txt', encoding = 'utf-8') as f:
    s = f.read()
    # print(s)

# find = 'абв' 
# if find in s:
#     print('true')

ns = s.replace('абв', '')
# print(ns)

with open('new_text.txt','w', encoding = 'utf-8') as f:
    f.write(ns)