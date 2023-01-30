s1 = ' '.join([input(), 'запретил букву'])

unique = []

for i in s1:
    if(i not in unique and i!=' '):
        unique.append(i)


for i in sorted(unique):
    print(' '.join([s1,i]))
    s1 = s1.replace(i, '').strip()
