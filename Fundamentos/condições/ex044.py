print('=========== LOJAS HENRIQUE ===========  ')
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[  1  ] à vista dinheiro/cheque')
print('[  2  ] à vista cartao')
print('[  3  ] 2x no cartao')
print('[  4  ] 3x ou mais no cartao')

opcao = int(input('Qual é a opção? '))

if opcao == 1: 
    preço = valor * 0.90
    print(f'Sua compra de R${valor} vai custar R${preço} no final. ')

elif opcao == 2:
    preço = valor * 0.95
    print(f'Sua compra de R${valor} vai custar R${preço} no final. ')    

elif opcao == 3:
    print(f'Sua compra de R${valor} vai custar R${valor} no final. ')  

elif opcao == 4:
    preço = valor * 1.20
    parcelas = int(input('Em quantas vezes voce quer dividir? '))
    valor = preço / parcelas
    print(f'Sua compra sera parcelada em {parcelas}x de R${valor} com juros')
    print(f'Sua compra de R${valor} vai custar R${preço} no final. ')    

