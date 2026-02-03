matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0],]
somas = []
coluna = 0 

for l in range(0, 3): 
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somas.append(matriz[l][c])

print('-=' * 20 )

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 20)

print(f'A Soma dos numeros pares é {sum(somas)}')

for l in range(0, 3):
    coluna += matriz[l][2]

print(f'A soma dos valores da terceira coluna é {coluna}.')

for c in range(0 ,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c]:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
