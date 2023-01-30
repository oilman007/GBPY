
# еще ДЗ...
n = int(input("Введите число N: "))
i = 2 
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")
