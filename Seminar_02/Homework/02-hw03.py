# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# 6 => [2.0, 2.25, 2.37, 2.441, 2.488, 2.522] - 14.071

number = int(input('Введите натуральное число: '))
if number < 1:
    print("Введено некорректное число")
else:
    number_list = []
    sum = 0
    for i in range(1, number + 1):
        temp = round((1 + 1/i)**i, 3)
        number_list.append(temp)
        sum = sum + temp
    print(number_list)
    print(round(sum, 3))