# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)


import random

def get_array(size, min, max):
    array = []
    for i in range(size):
        array.append(random.randrange(min,max+1))
    return array

def get_mix(array):
    size = len(array)
    for i in range(size):
        for j in range(size):
            swap(array,i,random.randrange(0,size))
    return array

def swap(array,i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

n = int(input('enter N '))

array = get_array(size = n, min = 0, max = n)
print(array)

mix = get_mix(array)
print(mix)
