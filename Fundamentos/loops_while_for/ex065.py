resp = 'S'
soma = quant = media = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor: 
            menor = num
    resp = str(input('Quer Continuar [S/N] ')).upper()
media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media} ')
print(f'O maior valor foi {maior} e o menor foi {menor}')