valores = []

for v in range(0, 5):
    numero = int(input(f'Digite um valor para a Posição {v}: '))
    valores.append(numero)

print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ')
print(f'O menor valor digitado foi {min(valores)}')