import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

op = math.pow(oposto, 2)
ad = math.pow(adjacente, 2)

hipo = op + ad
resultado = math.sqrt(hipo)
print(f'A hipotenusa vai medir {resultado:.2f}')