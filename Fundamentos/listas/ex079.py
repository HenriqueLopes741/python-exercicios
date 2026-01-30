lista = []
escolha = ' '

while True:
    a = int(input('Digite um valor: '))
    print('Valor adicionado com sucesso...')
    lista.append(a)
    escolha = str(input('Quer continuar? [S/N]')).upper()
    if escolha == 'S':
        print()
    else: 
        break

print(lista)

