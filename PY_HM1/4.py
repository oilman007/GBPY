# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).



#  2 | 1
#  --+--
#  3 | 4

area = float(input('enter area number (1-4) '))

if area == 1:
    print("0 < x < infinity   and   0 < y < infinity")
elif area == 2:
    print("-infinity < x < 0   and   0 < y < infinity")
elif area == 3:
    print("-infinity < x < 0   and   -infinity < y < 0")
elif area == 4:
    print("0 < x < infinity   and   -infinity < y < 0")
else:
    print("unknown")