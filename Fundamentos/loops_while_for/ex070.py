total = caro = cont = totmil  = menor =  0
barato = ''

print('-' * 40 )
print('         LOJA SUPER BARATAO       ')
print('-' * 40 )

while True: 
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
    else: 
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper()
    if resp == 'N':
        break
print('      Fim do programa     ' )
print(f'O total da compra foi R${total}')
print(f'Temos {totmil} produtos custando mais de R$1000.100')
print(f'O produto mais barato foi {barato} que custa R${menor}')