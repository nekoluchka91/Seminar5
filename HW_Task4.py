# Домашняя задача 4. Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся 
# в отдельных текстовых файлах.

def encode(text):
    encoded_str = ''
    i = 0
    while i <= len(text) - 1:
        count = 1
        char = text[i]
        j = i
        while j < len(text) - 1:
            if text[j] == text[j + 1]:
                count += 1
                j += 1
            else:
                break
        encoded_str = encoded_str + str(count) + char
        i = j + 1
    return encoded_str

def decode(RLE_text):
    decoded_text = ''
    i = 0
    j = 0
    while i <= len(RLE_text) - 1:
        count = int(RLE_text[i])
        char = RLE_text[i + 1]
        for j in range(count):
            decoded_text = decoded_text + char
            j += 1
        i += 2
    return decoded_text

text = input('Введите исходный текст для сжатия через RLE-алгоритм: ')
rle_text = encode(text)
back_to_text = decode(rle_text)

print(f'Сжатие: [{rle_text}]')
print(f'Восстановление исходного текста: [{back_to_text}]')