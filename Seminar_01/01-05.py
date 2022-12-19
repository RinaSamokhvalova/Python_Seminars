n = int(input('Введите число: '))

if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print("yes")
else:
    print("no")