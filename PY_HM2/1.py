#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

txt = input('enter value ')

sum = 0
for t in txt:
     if t.isdigit():
        sum += int(t)

print(f'sum = {sum}')