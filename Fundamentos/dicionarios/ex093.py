info = dict()

info['nome'] = str(input('Nome do jogador: '))
info['partidas'] = int(input(f'Quantas partidas {info["nome"]} jogou?: '))

gols = []  # lista para guardar gols por partida

for c in range(info["partidas"]): 
    gol = int(input(f'Quantos gols na partida {c + 1}: '))
    gols.append(gol)

info['gols'] = gols
info['total'] = sum(gols)  

print('-='*20)
print(info)
print('-=' * 30)
print(f'O jogador {info["nome"]} jogou {info["partidas"]} partidas.')


for i, g in enumerate(info['gols']):
    print(f'  => Na partida {i + 1}, fez {g} gol(s).')

print(f'Total de gols: {info["total"]}')