# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# in
# Enter the name of the file with the text: 'text_words.txt'
# Enter the file name to record: 'text_code_words.txt'
# Enter the name of the file to decode: 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

def file_creating (spisok, file_text = 'text_words.txt'): # запись в файл
    with open(file_text, 'w', encoding="utf-8") as data:
        for i in range(len(spisok)):
            data.write(spisok[i] + '\n')

def file_reading (file_text = 'text_words.txt'):        # чтение из файла
    with open(file_text, 'r', encoding="utf-8") as file_tx:
        return [stroki.strip() for stroki in file_tx]
        

def RLE_compression (list_text):        # кодирование списка слов
    list_result = []
    for i in range(len(list_text)):
        temp_text = list_text[i]
        temp_el = temp_text[0]
        count = 1
        result = ''
        for j in range(1, len(temp_text)):
            if temp_el == temp_text[j]:
                count = count + 1
            else:
                result = result + str(count) + temp_el
                count  = 1
                temp_el = temp_text[j]
        result = result + str(count) + temp_el
        list_result.append(result)
    return list_result

def RLE_decompression (list_text):      # декодирование списка слов
    list_result = []
    for j in range(len(list_text)):
        num = ''
        decode_result = ''
        decode = list_text[j]
        for i in range(len(decode)):
            if decode[i].isdigit():
                num = num + decode[i]
            else:
                decode_result = decode_result + int(num) * decode[i]
                num = ''
        list_result.append(decode_result)
    return list_result

# создадим исходный файл
# lst=['aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaavbbwwPPuuuTTYyWWQQ', 'ooooiiiiyyvrrrrrr', 'gggggggwwwwwvvvviiixxxx']
# file_creating(lst)

lst = file_reading()
print(lst)
lst = RLE_compression(lst)
print(lst)
file_creating(lst, 'text_code_words.txt')
print('А теперь наоборот:')
lst = file_reading('text_code_words.txt')
print(lst)
lst = RLE_decompression(lst)
file_creating(lst, 'text_decode_words.txt')
print(lst)