# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

#  2 | 1
#  --+--
#  3 | 4

x = float(input('enter x '))
y = float(input('enter y '))

if x > 0 and y > 0:
    print("#1")
elif x < 0 and y > 0:
    print("#2")
elif x < 0 and y < 0:
    print("#3")
elif x > 0 and y < 0:
    print("#4")
else:
    print("unknown")