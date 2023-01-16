# 2. Задайте натуральное число N. 
#    Напишите программу, которая составит список простых множителей числа N.

# 54 >> [2, 3, 3, 3]
# 9990 >> [2, 3, 3, 3, 5, 37]
# 650 >> [2, 5, 5, 13]

def list_primes (n: int):
    spisok = []
    spisok.append(2)
    for i in range(3, n+1):
        flag = True
        for j in range(len(spisok)):
            if not(i%spisok[j]):
                flag = False
        if flag:
            spisok.append(i)
    return spisok

def find_prime_divisors (n: int):
    spisok = list_primes(n)
    result = []
    for i in range(len(spisok)):
        while not(n % spisok[i]):
            result.append(spisok[i])
            n = n/spisok[i]
    return result

number = int(input("Enter a natural number: "))
print(find_prime_divisors(number))
