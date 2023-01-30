# еще ДЗ
from random import randint
 
array_int = [randint(0, 10) for i in range(20)]
new_array = [item for item in array_int if array_int.count(item) == 1]
print(array_int)
print(new_array)
