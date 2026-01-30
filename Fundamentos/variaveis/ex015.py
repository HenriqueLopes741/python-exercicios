dias = int(input('Quantos dias foram alugados? '))
km = int(input('Quantos km foram rodados? '))

valord = 60 * dias
valorkm = km * 0.15
total = valord + valorkm

print(f'O total a pagar é de R${total}')
