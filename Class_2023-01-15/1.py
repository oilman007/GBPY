
# дз про Пи
a = int(input('введите нужную точность 1#= '))
pi_target = 0
for i in range(1, 1000000):
     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
print(str(pi_target)[:a + 2])
