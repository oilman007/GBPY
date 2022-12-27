#     Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#     Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def get_array(size, min, max):
    array = []
    for i in range(size):
        array.append(random.randrange(min,max+1, 2))
    return array


a = get_array(5, 1, 10)    
print(a)

s = 0
for i in range(1, len(a), 2):
    s+= a[i]

print(s)
