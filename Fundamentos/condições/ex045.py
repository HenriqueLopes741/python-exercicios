import time
import random

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual é a sua jogada? '))

print('-=' * 20)

if jogador < 0 or jogador > 2:
    print('Jogada inválida')
else:
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 20)

    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')

    if computador == jogador:
        print('EMPATE')

    elif computador == 0:  # Pedra
        if jogador == 1:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')

    elif computador == 1:  # Papel
        if jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')

    elif computador == 2:  # Tesoura
        if jogador == 0:
            print('JOGADOR VENCE')
        else:
            print('COMPUTADOR VENCE')
