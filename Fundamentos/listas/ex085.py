pares = []
impares = []

for c in range(1, 8):
    numero = int(input(f'Digite o {c}o, valor: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')