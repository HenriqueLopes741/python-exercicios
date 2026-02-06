from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}

ranking = list()

print('Valores sorteados: ')

for k, v in jogo.items():
    sleep(1)
    print(f'Jogador {k} tirou {v} no dado. ')
    
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)
print('-=' * 30)
print('== RANIKNG DOS JOGADORES == ')
print('-=' * 30)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)