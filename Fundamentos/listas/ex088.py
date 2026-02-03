from random import randint

matriz = []
jogos = []

print('-=' * 20)
print('        JOGO NA MEGA SENA     ')
print('-=' * 20)

quantidade = int(input('Quantos jogos você quer que eu faça? '))
tot = 0

while tot < quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in matriz:
            matriz.append(num)
            cont += 1
        if cont == 6:
            break
    matriz.sort()
    jogos.append(matriz[:])
    matriz.clear()
    tot += 1

print('-=' * 30)
print(f'SORTEANDO {quantidade} JOGOS')
print('-=' * 30)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
