ano = int(input('Em que ano você nasceu? '))

idade = 2026 - ano

if idade <= 9:
    print(f'Voce tem {idade} anos e voce esta na categoria MIRIM')
elif idade <= 14:
    print(f'Voce tem {idade} anos e voce esta na categoria INFANTIL')
if idade <= 19:
    print(f'Voce tem {idade} anos e voce esta na categoria JUNIOR')
elif idade <= 25:
    print(f'Voce tem {idade} anos e voce esta na categoria SENIOR')
else: 
    print(f'Voce tem {idade} anos e voce esta no MASTER')
