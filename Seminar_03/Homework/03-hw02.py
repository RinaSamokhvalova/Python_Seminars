# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in >> 4
# out
# >> [2, 5, 8, 10]
# >> [20, 40]

# in >> 5
# out
# >> [2, 2, 4, 8, 8]
# >> [16, 16, 4]

import random

def new_list (count):
    result_list = []
    for i in range(count):
        result_list.append(random.randrange(11))
    return result_list

def product_pairs_list (spisok):
    change_list = []
    len_spisok = len(spisok)
    for i in range(len_spisok // 2):
        change_list.append(created_list[i]*created_list[len_spisok - 1 - i])
    #if len_spisok // 2 != len_spisok / 2: #Проверка на нечетность
    if len_spisok % 2: #Проверка на нечетность
        change_list.append(created_list[len_spisok // 2])
    return change_list

count = int(input("Number of numbers: "))
if count < 0:
    print ("Negative value of the number of numbers!")
else:
    created_list = new_list(count)
    print (created_list)
    print (product_pairs_list(created_list))