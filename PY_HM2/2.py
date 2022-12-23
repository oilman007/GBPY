#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


value = int(input('enter value '))

result = []

for i in range(1, value+1):
    temp = 1
    for j in range(1, i+1):
        temp *= j
    result.append(temp)
    

print(result)