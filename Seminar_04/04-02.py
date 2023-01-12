# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

from math import sqrt

def quadratic_equation(a, b, c):
    if a == 0:
        with open('file_04-02.txt', 'a', encoding="utf-8") as data:
            data.write (f"\nОшибка! {a}x² + {b}x + {c} = 0 - не квадратное уравнение!\n")
        return
    d = b**2 - 4 * a * c
    with open('file_04-02.txt', 'a', encoding="utf-8") as data:
        data.write (f"\n{a}x² + {b}x + {c} = 0\n") # \n - перевод коретки на новую строку
        if d > 0 and a:
            # x1 = round((-b - d**(0.5))/(2*a), 2)
            # x2 = round((-b + d**(0.5))/(2*a), 2)
            x1 = round((-b - sqrt(d))/(2*a), 2)
            x2 = round((-b + sqrt(d))/(2*a), 2)
            data.write(f"Уравнение имеет два корня: х1 = {x1} и х2 = {x2}\n")
        elif d == 0 and a:
            x = -b/(2*a)
            data.write(f"Уравнение имеет единственное решение: {x}\n")
        else:
            data.write("Дискриминант меньше нуля - уравнение не имеет решений\n")

# quadratic_equation(1, 2, -3)
# quadratic_equation(5, 6, -7)
# quadratic_equation(8, 9, -10)
quadratic_equation(int(input("A = ")), int(input("B = ")), int(input("C = ")))