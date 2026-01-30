import math

n1 = int(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tang = math.tan(math.radians(n1))

print(f'O ângulo de {n1} tem o SENO de {seno:.2f}')
print(f'O ângulo de {n1} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {n1} tem a TANGENTE de {tang:.2f}')
