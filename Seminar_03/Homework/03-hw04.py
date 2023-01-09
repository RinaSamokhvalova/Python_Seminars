# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in >> 5
# out >> [5.16, 8.62, 6.57, 7.92, 9.22]
#     >> Min: 0.16, Max: 0.92. Difference: 0.76

import random

def new_list (count):
    result_list = []
    for i in range(count):
        result_list.append(round(random.random()*10, 2)) # Случайные числа [0;10] с округлением до сотых
    return result_list

def changelist (spisok):
    change_list = []
    for i in range(count):
        change_list.append(int(spisok[i]*100)%100 /100)
    print (change_list)

    min = change_list[0]
    max = change_list[0]
    for i in range(1, count):
        if min > change_list[i]:
            min = change_list[i]
        if max < change_list[i]:
            max = change_list[i]
    print(f'Min: {min}, Max: {max}. Difference: {round(max-min,2)}')


count = int(input("Number of numbers: "))
if count < 0:
    print ("Negative value of the number of numbers!")
else:
    created_list = new_list(count)
    print (created_list)
    changelist(created_list)

    
