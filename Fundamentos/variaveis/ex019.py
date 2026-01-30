import random

n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

nomes = [n1,n2,n3,n4]
sorteado = random.choice(nomes)
print(f'O nome sorteado é {sorteado}')