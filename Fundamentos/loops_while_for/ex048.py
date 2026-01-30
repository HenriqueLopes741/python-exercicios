soma = 0
conta = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        conta = conta + 1
        soma = soma + c 
print(f'A soma de todos os valores é {soma}')
