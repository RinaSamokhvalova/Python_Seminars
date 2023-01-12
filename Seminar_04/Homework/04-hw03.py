# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности в том же порядке.
# 7 >> [4, 5, 3, 3, 4, 1, 2] >> [5, 1, 2]
# 10 >> [4, 4, 5, 5, 6, 2, 3, 0, 9, 4] >> [6, 2, 3, 0, 9]
# -1 >> Negative value of the number of numbers! >> []

import random

def create_list (n: int):
    result_list = []
    for i in range(n):
        result_list.append(random.randrange(11))
    return result_list

def change_list (spisok: list):
    result_list = []
    for i in range(len(spisok)):
        if spisok.count(spisok[i]) == 1:
            result_list.append(spisok[i])
    return result_list

number = int(input("Enter a natural number: "))
if number < 0:
    print("Negative value of the number of numbers!")
else:
    new_lst = create_list (number)
    print(new_lst)
    print(change_list(new_lst))