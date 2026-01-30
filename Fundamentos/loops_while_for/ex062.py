print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)


p1 = int(input('Primeiro Termo: '))
r = int(input('Segundo termo: '))
termo = p1
cont = 1
total = 0
mais = 10 
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo = termo + r
        cont += 1
    print('FIM')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))