# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# 88 -> 1011000
# 11 -> 1011
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def ConvertNumberBinary (numberDec):
    number_list = []
    while numberDec != 0:
        number_list.append(str(numberDec % 2))
        numberDec = numberDec // 2
    # number_list.reverse()
    number_list2 = []
    for i in range(len(number_list)-1, -1, -1):
        number_list2.append(number_list[i])
    return number_list2

print (int(''.join(ConvertNumberBinary(int(input('Введите натуральное число: '))))))
