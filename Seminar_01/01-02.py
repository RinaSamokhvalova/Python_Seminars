# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
	
maxim = 0
for i in range(5):
    print('Введите число:')
    num = int(input())
    if num > maxim:
        maxim = num

print(f'Максимальное число: {maxim}')
