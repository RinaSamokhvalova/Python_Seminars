# 3. На вход программе подается число n.
#    Программа печатает численный треугольник.
#    Используем вложенные циклы.
# 5 >>
#       >> 1
#       >> 22
#       >> 333
#       >> 4444
#       >> 55555

def numerical_triangle (number: int):
    s=""
    for i in range(1, number + 1):
        for j in range(i):
            s = s + str(i)
        print(s)
        s=""
    return

def numerical_triangle2 (number: int):
    s=""
    for i in range(1, number + 1):
        for j in range(i):
            print(i, end="")
        print()
    return

numerical_triangle (int(input("Введите натуральное число: ")))
numerical_triangle2 (int(input("Введите натуральное число: ")))