# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

with open('PYTHONDZ#5/Zadacha2_RLE_1.txt', 'r') as data:
    my_text = data.read()
with open('PYTHONDZ#5/Zadacha2_RLE_2.txt', 'r') as data:
    my_text2 = data.read()
str_code = encode_rle(my_text)
print(str_code)
str_decode = decoding_rle(my_text2)
print(str_decode)