casa = int(input('Valor da casa: R$'))
salario = int(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

meses = anos * 12
prestacao = casa / meses
limite = salario * 0.30

if prestacao <= limite:
    print(f'O emprestimo sera concedido')
else:
    print(f'O emprestimo foi negado')