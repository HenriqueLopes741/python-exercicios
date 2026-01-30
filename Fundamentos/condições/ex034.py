salario = int(input('Qual é o valor do seu salario? '))

if salario >= 1250:
    aumento = salario * 1.1
    print(f'Voce antes recebia {salario} com o aumento {aumento:.2f}')
else:
    aumento = salario * 1.15
    print(f'Voce antes recebia {salario} com o aumento {aumento:.2f}')    