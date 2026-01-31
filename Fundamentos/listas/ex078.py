val = []

for v in range(0, 5):
    numero = int(input(f'Digite um valor para a Posição {v}: '))
    val.append(numero)

print(f'Voce digitou os valores {val}')
print(f'O maior valor digitado foi {max(val)} nas posições ')
print(f'O menor valor digitado foi {min(val)}')