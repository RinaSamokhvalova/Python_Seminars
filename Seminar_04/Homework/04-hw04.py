# 4*. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз.
# in >> out in the file
# 9  >> 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 5  >> 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 3  >> 4*x^2 - 4 = 0
# 0  >> ""
# -1 >> ""
# 4  >> 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

import random

def create_list (n: int):
    result_list = []
    for i in range(n):
        if i == n-1:
            temp = random.randrange(11)
            while temp == 0:
                temp = random.randrange(11)
            result_list.append(temp)
        else:
            temp = random.randrange(11)
            result_list.append(temp)
    return result_list

def create_polynom (spisok: list):
    result_str = ''
    for i in range(len(spisok)-1, 0, -1):
        if result_str == '' and spisok[i] !=0:
            result_str = result_str + str(spisok[i]) + '*x^' + str(i)
        elif result_str != '' and spisok[i] !=0:
            result_str = result_str + ' + ' + str(spisok[i]) + '*x^' + str(i)
    if spisok[0] !=0:
        result_str = result_str + ' + ' + str(spisok[0]) + ' = 0'
    else: result_str = result_str + ' = 0'
    return result_str

number = int(input("Введите количество многочленов для формирования: "))
if number > 0:
    list_polynomial = []
    with open('file_04-hw04.txt', 'a', encoding="utf-8") as data:
        
        for i in range(number):
            list_polynomial = create_list(int(input("Введите степень многочленоа: ")))
            # data.writelines (create_polynom(list_polynomial))
            data.write (f'{create_polynom(list_polynomial)}\n')
else: print("Введено некоректное число! ")