# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# *Пример:*
#      in  -> out
# -   6782 -> 23
# -   0.67 -> 13
# - 198.45 -> 27

number = float(input('Введите вещественное число: '))
temp_number = number
flag = False
count = 0
while flag == False:
    if round(temp_number, count) == temp_number:
        flag = True
    else:
        count = count + 1
temp_number = number * 10**count
count = 0
sum = 0
while temp_number != 0:
    sum = sum + temp_number % 10
    temp_number = temp_number // 10

print(f"Сумма цифр числа {number} равна {int(sum)}")