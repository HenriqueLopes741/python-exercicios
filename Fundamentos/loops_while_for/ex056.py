total = 0
idade_mais_velho = 0
nome_mais_velho = ''

for p in range(1, 5):
    print(f'-------- {p}ª PESSOA ---------')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    total += idade

    if sexo == 'M' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

media = total / 4

print(f'A média de idade do grupo é {media}')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}')
