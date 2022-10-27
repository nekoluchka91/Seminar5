# Задача 1. В файле находится N натуральных чисел, 
# записанных через пробел. 
# Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

# path = 'file_prac1.txt'
# data = open(path, 'r')
# lst = f.read().split()

string = '1 2 3 5 6 7'

lst = list(map(int, string.split()))

for i in range(1, len(lst)):
    if lst[i] - 1 != lst[i-1]:
        print(lst[i] - 1)