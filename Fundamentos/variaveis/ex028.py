import random 
import time
print('--------------------------------------------------------')

print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('--------------------------------------------------------')

n = random.randint(0, 5 )
escolhido = int(input('Escolha um numero entre 0 e 5: \n'))
print('Processando...')
time.sleep(3)
if n == escolhido:
    print('Parabens você acertou o numero')
else:
    print(f'O numero que pensei era {n}\nTente novamente')

