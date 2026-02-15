from random import randint
num = list()


def sortear(lista):
    print('Sorteando 5 valores da lista: ')
    for cont in range(1, 6):
        lista.append(randint(1, 10))

def somarPar(lista):
    soma = 0 
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos  somasssss {soma}')



sortear(num)
print(num)
somarPar(num)