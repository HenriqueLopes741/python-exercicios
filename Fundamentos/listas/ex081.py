lista = []
escolha = ' '

while True: 
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    escolha = str(input('Quer continuar? [S/N] ')).upper()

    if escolha == 'S':
        print('')
    else:
        print('Colque uma escolha valida')
        break

print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista} ')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O 5 nao faz parte da lista')