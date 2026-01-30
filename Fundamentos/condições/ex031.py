km = int(input('Quantos km você viajou? '))

if km < 200:
    valor = km * 0.50
    print(f'Voce pagara R${valor}')
else:
    valor = km * 0.45
    print(f'Você ganhou desconto de 5 centavos R${valor}')