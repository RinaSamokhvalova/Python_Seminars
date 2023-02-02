# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

# in: "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out: {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

from itertools import groupby

def create_dictionary(spisok: list):
    return {k[0]: list(filter(lambda el: el[0] == k[0], spisok)) for k in sorted(spisok)} 

original_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(create_dictionary(original_list))

exit()

def create_dictionary(spisok: list):
    result = {}
    if spisok:
        spisok = sorted(spisok)
        for el in spisok:
            key = el[0]
            if key in result:
                result[key] += [el]     #добавляем элмент в список в конец
            else:
                result[key] = [el]
    return result


original_list = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
print(create_dictionary(original_list))