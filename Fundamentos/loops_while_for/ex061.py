print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)


p1 = int(input('Primeiro Termo: '))
r = int(input('Segundo termo: '))
termo = p1
cont = 1

while cont <=10:
    print(f'{termo} → ', end='')
    termo = termo + r
    cont += 1
print('FIM')

