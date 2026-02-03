lista1 = []
lista2 = []

while True:
    lista1.append(str(input('Nome: ')))
    lista1.append(float(input('Peso: ')))
    lista2.append((lista1[:]))
    lista1.clear()

    resposta = str(input(('Quer continuar? [S/N] ')))
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'Os dados foram {lista1} ')
print(f'Ao todo, você cadastrou {len(lista2)} pessoas')
