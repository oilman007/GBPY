# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.


x1 = bool(input('enter x1 '))
x2 = bool(input('enter x2 '))
x3 = bool(input('enter x3 '))

c1 = not (x1 or x2 or x3)
c2 = not x1 and not x2 and not x3

print(f'condition#1 is {c1} = not ({x1} or {x2} or {x3})')
print(f'condition#2 is {c2} = not {x1} and not {x2} and not {x3}')
print(f'condition#1 == condition#2 is {c1==c2}')