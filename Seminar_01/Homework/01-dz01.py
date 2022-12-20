# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*
# 7 -> “Weekend”
# 1 -> “Workday”
# 63 -> “It’s not a day of the week!”

n = int(input('Enter a number representing the day of the week: '))
if 1 <= n <= 5:
    print("Workday")
elif 6 <= n <= 7:
    print("Weekend")
else:
    print("It's not a day of the week!")
