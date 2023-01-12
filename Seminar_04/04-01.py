# 1. Задайте строку из набора чисел. 
#    Напишите программу, которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

def str_to_list (stroka: str):
    new_str = stroka.split() # split - разбивает строку на список по заданнлму символу (по умолчанию по пробелам)
    spisok = []
    for i in range(len(new_str)):
        new_str[i] = new_str[i].strip(".,;:?!") # strip - удаляет из строки перечисленные элементы, по краям (не в середине)
        # добавляем отрицательные числа
        if new_str[i].replace("-", "", 1).isdigit():    # isdigit() - проверяет (True - если все символы в строке являются цифрами; False - если хотя бы один символ не является цифрой)
                                                        # replace() - возвращает копию строки, в которой все вхождения подстроки заменяются другой подстрокой.
            spisok.append(new_str[i])
    return spisok

def find_max_min (str_list: list):
    if str_list:
        return max(str_list, key=int), min(str_list, key=int)  # min & max - ищут минимальную и максимальную строку в списке, 
                                                                # параметр key=int позволяет рассматривать строки как числа
    print("The data is incorrect")
    return []

# input_str = input("Enter the numbers separated by a space: ")
input_str = "1, 3, 5, 63; 23! -34 444, 0.5 -40,5"
#print (str_to_list(input_str))
print (find_max_min ((str_to_list(input_str))))