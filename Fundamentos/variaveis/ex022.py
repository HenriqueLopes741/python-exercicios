nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print(f'Seu nome em maiusculo é {nome.upper()}') 
print(f'Seu nome em minusculo é {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome)} letras')
fonte  = nome.split()[0]
print(f'Seu primeiro nome é {fonte} e ele tem {len(fonte)} letras')