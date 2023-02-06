# 5**. Даны два файла, в каждом из которых находится запись многочленов. 
#      Задача - сформировать файл, содержащий сумму многочленов.
# 
# in "poly.txt", "poly_2.txt"
# out in the file:
#       3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0 
#       4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
#       4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0
# 
# in "poly.txt", "poly_2.txt"
# out >> The contents of the files do not match!

def reading_file(name1: str = 'file_04-hw05a.txt', name2: str = 'file_04-hw05b.txt', name3: str = 'file_04-hw05_res.txt'):
    data = open(name1, 'r')
    list1 = []
    for line in data:
        if line:
            list1.append(line.strip())
    data.close()

    data = open(name2, 'r')
    list2 = []
    for line in data:
        if line:
            list2.append(line.strip())
    data.close()

    if len(list1) == len(list2):
        data = open(name3, 'a', encoding="utf-8")
        for i in range(len(list1)):
            data.write (f"{list1[i][:-4] + ' + ' + list2[i]}\n")
        data.close()
    
reading_file()
