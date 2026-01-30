import time

lista = []

for c in range (0, 5):
    a = int(input('Digite um valor: '))
    lista.append(a)
    #time.sleep(1)
    print('Adicionando ao final da lista...')
lista.sort(reverse=True)
print(f'Os valores digtados em ordem foram: {lista}')