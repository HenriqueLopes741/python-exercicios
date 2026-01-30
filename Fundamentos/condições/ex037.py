num = int(input('Digite um numero intero'))

print(' [ 1 ] Converter para BINARIO')
print(' [ 2 ] Converter para OCTAL')
print(' [ 3 ] Converter para HEXADECIMAL')

opcao = int(input('Sua opcão: '))
bina = bin(num)
octal = oct(num)
hexa = hex(num)

if opcao == 1:
    print(f'O numero {num} em Binario é {bina}')
elif opcao == 2:
    print(f'O numero {num} em OCTAL é {octal}')
elif opcao == 3:
    print(f'O numero {num} em HEXADECIMAL é {hexa}')
else:
    print('Voce nao escolheu uma OPÇÂO ACEITA')