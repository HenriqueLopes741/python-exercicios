import random

v = 0

while True: 
    print('=-'* 20)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-'* 20)

    robo = random.randint(0, 11)
    n1 = int(input('Diga um valor: '))
    tipo = str(input('Par ou Impar? [P/I]: ')).upper()
    total = n1 + robo
    a = ''

    while a not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).upper()
    print(f'Voce Jogou {n1} e o computador {robo} total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!!')
            v += 1
        else:
            print('Voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu!!')
            v += 1
        else:
            print('Voce Perdeu')
            break