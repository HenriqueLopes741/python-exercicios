n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 1


while opcao != 5:
    print('[ 1 ] somar ')
    print('[ 2 ] multiplicar ')
    print('[ 3 ] maior ')
    print('[ 4 ] novos numeros ')
    print('[ 5 ] sair do programa  ')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1: 
        soma = n1 + n2
        print(f'A soma dos dois numeros é {soma}')
    elif opcao == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação dos dois numeros {multiplicação} ')
    elif opcao == 3:    
        if n1 > n2:
            maior = n1
        else: 
            maior = n1
        print(f'O maior valor é {maior} ')
    elif opcao == 4:
        print('Informe novamente os numeros: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando')
    else: 
        print('Opção invalida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre! ')