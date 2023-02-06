# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Use comprehension.
# in: 9   >> out: [15, 16, 2, 3, 1, 7, 5, 4, 10] >> [16, 3, 7, 10]
# in: 10 >> out: [28, 20, 10, 5, 1, 24, 7, 15, 23, 25] >> [24, 15, 23, 25]

import random


def create_list(n: int, limit: int = 11):
    if n < 0:
        return []
    else:
        return [random.randint(0, limit) for i in range(number)]


def result_list(lst: list):
    return [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]


number = int(input("Enter a natural number: "))
new_lst = create_list(number)
print(new_lst)
print(result_list(new_lst))


exit()


def create_list(n: int):
    result_list = []
    for i in range(n):
        result_list.append(random.randrange(11))
    return result_list


def change_list(spisok: list):
    result_list = []
    for i in range(1, len(spisok)):
        if spisok[i] > spisok[i-1]:
            result_list.append(spisok[i])
    return result_list


number = int(input("Enter a natural number: "))
if number < 0:
    print("Negative value of the number of numbers!")
else:
    new_lst = create_list(number)
    print(new_lst)
    print(change_list(new_lst))
