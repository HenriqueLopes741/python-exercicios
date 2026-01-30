lista = []
escolha = ''
pares = []
impares = []
while True:
    numeros = int(input('Digite um numero: '))
    lista.append(numeros)
    escolha = str(input('Quer continuar? [S/N]')).upper()
    
    if escolha in 'Nn':
        break

print(f'A lista completa é {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista em pares é {pares}')
print(f'A lista de impares é {impares}')