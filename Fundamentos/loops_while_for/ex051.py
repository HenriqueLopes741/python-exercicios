p1 = int(input('Primeiro termo: '))
r = int(input('Primeiro Termo: '))

decimo = p1 + (10-1) * r

for c in range (p1, decimo + r, r):
    print(f'{c}', end=' → ')
print('ACABOU')