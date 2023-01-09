# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

# in >> 5
# out
# >> [10, 2, 3, 8, 9]
# >> 22

# in >> 4
# out
# >> [4, 2, 4, 9]
# >> 8

import random

def new_list (count):
    result_list = []
    for i in range(count):
        result_list.append(random.randrange(11))
    return result_list

def sum_number (spisok):
    sum = 0
    for i in range(0, len(spisok), 2):
        sum = sum + spisok[i]
    return sum

count = int(input("Number of numbers: "))
if count < 0:
    print ("Negative value of the number of numbers!")
else:
    created_list = new_list(count)
    print (created_list)
    print (sum_number(created_list))

