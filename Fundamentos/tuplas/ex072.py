extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',  'seis', 'sete', 'oito', 'nove', 'Dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

print(len(extenso))

while True:
    n1 = int(input('Digite um numero entre 0 e 20: '))
    if n1 <= 20:
       break
    print('Tente novamente') 
print(f'Voce digitou o numero {extenso[n1]}') 