# 4*. Напишите программу, которая принимает на вход 2 числа. 
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N]. 
# Найдите произведение элементов на указанных позициях (не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]	=> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]		=> There are no values for these indexes!

number = int(input('Введите натуральное число: '))
if number < 1:
    print("Введено некорректное число")
else:
    number_list = []
    for i in range(- number, number + 1):
        number_list.append(i)
    print(number_list)
    
    pos_1 = int(input('Введите позицию первого элемента: '))
    pos_2 = int(input('Введите позицию второго элемента: '))
    if 0 < pos_1 <= len(number_list) and 0 < pos_2 <= len(number_list):
        print(number_list[pos_1-1]*number_list[pos_2-1])
    else:
        print("Для этих индексов нет значений!")