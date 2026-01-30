from datetime import date

atual = date.today().year

maiores = 0
menores = 0 

for i in range(1, 8):
    ano = int(input(f'Em que ano a {i} pessoa nasceu? '))
    idade = atual - ano

    if idade >= 18:
        maiores += 1
    else:
        menores += 1


print(f'\n Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E tambem tivemos {menores}')
