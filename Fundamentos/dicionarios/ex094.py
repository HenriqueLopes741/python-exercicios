pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
while True: 
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
    if pessoa['sexo'] in 'MF':
        break
    print('ERRO! Por favor, digite apenas M ou F')