# 1. Создайте список из N натуральных чисел(0 до N), упорядоченных по возрастанию. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

# 10 >> [1, 2, 3, 4, 6, 7, 8, 9, 10, 11] >> 5
# 10 >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] >> -1 # -1 - ничего не найдено

# вариант 1
# import random
#  
# def create_list (n: int):
    # spisok = []              
    # for i in range(n + 1): 
    #     spisok.append(i)
    # spisok.remove(random.randrange(n + 1))
    # return spisok

from random import choice

def create_list (n: int):
    if n < 1:
        return []

    spisok = [i for i in range(n + 1)]
    spisok.remove(choice(spisok))
    return spisok


def search_number (spisok: list):
    for i in range(1, len(spisok)):
        if spisok[i] - 1 != spisok[i - 1]:
            return spisok[i] - 1
    return -1


cr_list = create_list(int(input("Введите натуральное число > 0: ")))
print(cr_list)
print(search_number(cr_list))
