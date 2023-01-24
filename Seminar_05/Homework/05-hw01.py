# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# >> Number of words: 10
# >> авб абв бав абв вба бав вба абв абв абв >> авб бав вба бав вба

# >> Number of words: 6
# >> ваб вба абв ваб бва абв >> ваб вба ваб бва

# >>  Number of words: -1
# >> The data is incorrect

from random import sample

def create_str(n: int, alph = 'abc', word = 3):
    result_str = ''
    for i in range(n):
        temp = sample(alph, word)
        result_str = result_str + "".join(temp) + ' '
    return result_str


def change_str(text: str, word = "abc"):
    text = text.replace(word, "")
    while text.find("  ") != -1:
        text = text.replace("  ", " ")
    text = text.strip()
    return text
    

number = int(input("Enter a natural number: "))
if number < 0:
    print("Negative value of the number of numbers!")
else:
    new_str = create_str(number)
    print(new_str)
    # stroka = input("Enter a word: ")
    # print(change_str(new_str, stroka)) 
    print(change_str(new_str)) 