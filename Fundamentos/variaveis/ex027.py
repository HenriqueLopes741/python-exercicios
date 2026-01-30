n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
# Use o índice -1 para pegar sempre o último elemento de forma simples
print(f'Seu último nome é {nome[-1]}')
