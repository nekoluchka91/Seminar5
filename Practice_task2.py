# Задача 2. Дан список чисел. 
# Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]

result = [lst[0]] # индекс первого элемента [0] = эл-т 1

for item in lst:
    if item > result[len(result) - 1]: # индекс последнего элемента = 7
        result.append(item)

print(result)


# В случае, если первое число будет самое большое:
# lst = [87, 5, 2, 3, 4, 6, 1, 7]

# for i in range(len(lst)):
#     result = [lst[i]] 
#     for j in range(i, len(lst)):
#         if lst[j] > result[len(result) - 1]:
#             result.append(lst[j])
#     if len(result) != 1:
#         break

# print(result)


# РЕШЕНИЕ В ОДНУ СТРОКУ:
# lst = [1, 5, 2, 3, 4, 6, 1, 7]

# first = lst[0]

# result = [first := num for num in lst if num >= first]
# маржовый оператор := позволяет определить переменную и 
# тут же вернуть ее значение
# print(result)


# СПИСОК ВСЕХ!!!! КОМБИНАЦИЙ ВОЗРАСТАЮЩИХ ПОСЛЕДОВАТЕЛЬНОСТЕЙ
# lst = [1, 5, 2, 3, 4, 6, 1, 7]
# array = []
# for i, el1 in enumerate(lst):
#     for j, el2 in enumerate(lst[i:]):
#         first = el1
#         seq = [first] + [first := num for num in lst[j:] if num > first]
#         if seq not in array and len(seq) > 1:
#             array.append(seq)
# print(*array, sep='\n')