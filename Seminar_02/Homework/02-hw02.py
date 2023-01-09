# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1,  2 - 1 * 2,  3 - 1 * 2 * 3,  4 - 1 * 2 * 3 * 4 и т.д.
# 4 -> [1, 2, 6, 24]
# 6 -> [1, 2, 6, 24, 120, 720]

number = int(input('Введите натуральное число: '))
if number < 1:
    print("Введено некорректное число")
else:
    number_list = []
    for i in range(1, number + 1):
        product = 1
        for j in range(1, i + 1):
            product = product * j
        number_list.append(product)
    print(number_list)