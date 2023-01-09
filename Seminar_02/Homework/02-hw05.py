# 5** . Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# in:	 10
# out:	-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]		=> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
number = int(input('Введите натуральное число: '))
number_list = []
for i in range(number):
    number_list.append(i)
print(number_list)

for i in range(number-1):
    index = random.randint(i+1, number-1)
    temp = number_list[i]
    number_list[i] = number_list[index]
    number_list[index] = temp

print(number_list)
