# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import sample

def new_spisok (count, alphabet = "abc"):
    new_list = []
    for i in range(count):
        temp = sample(alphabet, k=3)        # получили список букв
        new_list.append("".join(temp))      # соединили список букв в слово
    return new_list

def index_find (word, str_list):
    if word in str_list and str_list.count(word) > 1:
        index1 = str_list.index(word)
        print (str_list.index(word), index1 + 1)
    else: 
        print(-1)

spisok = new_spisok(int(input("Введите количество слов в списке: ")))
print (spisok)
index_find (input("Введите искомое слово: "), spisok)
