def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')

print('-' * 30)
a = str(input('Nome do Jogador: '))
b = str(input('Numero de Gols: '))
print('-' * 30)


if b.isnumeric():
    b = int(b)
else:
    b = 0
if a.strip() == '':
    ficha(a, b)
else:
    ficha(a, b)


