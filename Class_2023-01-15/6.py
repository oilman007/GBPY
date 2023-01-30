sasha = '1 5 15 20 10 50'
gala = '2 5 25 10 20'



f = lambda x: list(filter(lambda a: int(a)%2 == 0, x.split(" ")))
result = set(f(sasha)).intersection(set(f(gala)))

print(*sorted(list(result)))
