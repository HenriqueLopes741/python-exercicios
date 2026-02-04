ficha = list()


while True:
    nome = str(input('Nome: '))
    notas1 = float(input('Nota 1: '))
    notas2 = float(input('Nota 2: '))
    media = (notas1 + notas2) / 2

    ficha.append([nome, [notas1, notas2], media])

    escolha = str(input('Quer continuar? [S/N]'))
    
    if escolha in 'Nn':
        break

print('-='* 30 )
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-=' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 Interrompe)'))
    if opc == 999: 
        print('Finalizando...')    
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('<<<<< Volte SEMPRE >>>>>>')