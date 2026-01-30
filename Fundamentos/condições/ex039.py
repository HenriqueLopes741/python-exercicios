ano = int(input('Em que ano você nasceu? '))
idade = 2026 - ano

print(f'Você tem {idade} anos em 2026')

ano_alistamento = ano + 18

if idade == 18:
    print('Você deve se alistar ESTE ANO!')
    print(f'Seu alistamento é em {ano_alistamento}')

elif idade > 18:
    print('Você já deveria ter se alistado.')
    print(f'Você se alistou há {idade - 18} anos')
    print(f'Seu alistamento foi no ano de {ano_alistamento}')

else:
    print(f'Você ainda não precisa se alistar.')
    print(f'Faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento será no ano de {ano_alistamento}')
