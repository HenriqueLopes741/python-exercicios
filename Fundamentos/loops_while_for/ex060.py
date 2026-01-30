fat = int(input('Digite um numero para calcular seu fatorial: '))

c = fat
f = 1

print(f'Calculando {fat}! = ' , end='')

while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print(f'{f}!') 