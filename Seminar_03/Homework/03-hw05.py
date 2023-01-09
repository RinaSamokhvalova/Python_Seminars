# ** 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# 8 >> -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# 5 >>           5 -3 2 -1 1 0 1 1 2 3 5


def list_negaFibonacci (n):
    fibonacci_list = []
    fibonacci_list.append(0)
    fibonacci_list.append(1)
    nega_fibonacci_list = []
    nega_fibonacci_list.append(1)
    for i in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2])
        nega_fibonacci_list.append((-1)**(i+1)*fibonacci_list[i])
    nega_fibonacci_list.reverse()
    nega_fibonacci_list.extend(fibonacci_list)
    return nega_fibonacci_list


number = int(input("Number of numbers: "))
print(list_negaFibonacci(number))
