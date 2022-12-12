# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.


x1 = int(input('enter x1 '))
x2 = int(input('enter x2 '))
x3 = int(input('enter x3 '))

r1 = not (x1 or x2 or x3)
r2 = not x1 and not x2 and not x3

print(f'result is {r1==r2}')