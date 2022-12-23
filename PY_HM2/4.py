# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

import random



def get_array(size, min, max):
    array = []
    for i in range(size):
        array.append(random.randrange(min,max+1))
    return array

def get_ilist(lsize, asize):
    return  get_array(size=lsize, min=0, max = asize-1)

def get_product(array, ilist):
    result = 1
    for i in ilist:
        result *= array[i]
    return result

n = int(input('enter N '))

array = get_array(size = n, min = -n, max = n)
print(array)

ilist = get_ilist(random.randrange(2,n), n)
print(ilist)

print(get_product(array, ilist))