# 1. Вычислить число c заданной точностью d.

# Примеры:
# in  -> Enter a real number: 9
#        Enter the required accuracy '0.0001': 0.000001
# out -> 9.000000

# in  -> Enter a real number: 8.98785
#        Enter the required accuracy '0.0001': 0.001
# out -> 8.988

# # Подключаем класс Decimal из модуля decimal
from decimal import Decimal

def number_accuracy(n: Decimal, a: Decimal):
    return n.quantize(a)

number = Decimal(input("Enter a real number: "))
accuracy = Decimal(input("Enter the required accuracy '0.0001': "))
# print(number.quantize(accuracy))
print(number_accuracy(number, accuracy))