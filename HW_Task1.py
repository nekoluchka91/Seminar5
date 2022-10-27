# Домашняя задача 1. Напишите программу, 
# удаляющую из текста все слова, 
# в которых присутствуют все буквы "абв",
# но не обязательно в таком порядке.
# Напр., АВтоБус 

import re

str = 'автобус едет в страну абвгдейка а затем в страну бавария'
word = re.split('\W+', str)

el = ['а', 'б', 'в']

for i in range(len(word)):
    if word[i].find(el[0])!=-1 and word[i].find(el[1])!=-1 and word[i].find(el[2])!=-1:
       word[i] = ''

print(' '.join(word))

word = [i for i in word if i]
print(' '.join(word))


