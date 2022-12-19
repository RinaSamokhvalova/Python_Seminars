	# 3. Напишите программу, которая будет на вход принимать
	#    число N и выводить числа от -N до N

n = int(input('Введите число: '))

if n < 0:
    n = -n

# вариант 1
# i = - n
# while i <= n:
#     print(i)
#     i = i + 1

# вариант 2
# for i in range(-n, n + 1):
#     print(i)

# вариант 3
# print(list(range(-n, n + 1)))

# вариант 4
print(*range(-n, n + 1))