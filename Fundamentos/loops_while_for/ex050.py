soma = 0 
conta = 0
for c in range (1, 7):
    n1 = int(input(f'Digite o {c} valor: '))
    if n1 % 2 == 0:
        soma += n1
        conta += 1

print(f'Voce informou {conta} numeros e a soma foi {soma}')
        