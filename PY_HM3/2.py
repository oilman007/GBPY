# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def get_array(size, min, max):
    array = []
    for i in range(size):
        array.append(random.randrange(min,max+1))
    return array


def pair_mult(values):
    size = len(values)
    result = []
    for i in range(size//2):
        result.append(values[i] * values[size - i - 1])
    if size % 2 != 0:
        result.append(values[size//2 + 1] * 2) 
    return result

a = get_array(6, 1, 9)
print(a)

m = pair_mult(a)
print(m)