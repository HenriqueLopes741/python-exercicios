numero = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')) , 
          int(input('Digite mais um numero: ')),  int(input('Digite o ultimo numero numero: ')))

contagem = numero.count(9)
pares = [x for x in numero if x % 2 == 0 ]

print(f'Voce digitou os valores {numero}')
print(f'O valor 9 apareceu {contagem} vezes ')
if 3 in numero:
    print(f'O valor 3 apareceu na posição {numero.index(3)}')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram {pares} ')