# 2. Создайте список, в который попадают числа,
#    описывающие возрастающую последовательность.
#    Порядок элементов менять нельзя.
# Примеры:
# 8  >> [10, 0, 5, 11, 6, 1, 15, 10] >> [[10, 11, 15], [0, 5, 11, 15], [5, 11, 15], [11, 15], [6,15], [1,15]]
# 10 >> [19, 5, 1, 14, 5, 9, 15, 11, 12, 2] >> [[5, 14, 15], [1, 14, 15], [14, 15], [5, 9, 15], [9, 15], [11, 12]]

import random

def create_list (n: int):
    if n < 1:
        return []

    spisok = []              
    for i in range(n): 
        spisok.append(random.randrange(2*n))
    
    return spisok


def new_list (spisok: list):
    result = []
    for i in range(len(spisok)):
        temp = []
        temp.append(spisok[i])
        for j in range (i, len(spisok)):
            if spisok[j] > temp[len(temp)-1]:
                temp.append(spisok[j])
        if len(temp)>1:
            result.append(temp)
    return result


cr_list = create_list(int(input("Введите натуральное число > 0: ")))
print(cr_list)
print(new_list(cr_list))