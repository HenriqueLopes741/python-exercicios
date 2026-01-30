n = cont = total = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += n
    total += 1
print(f'A soma dos {total} valores foi {cont}')