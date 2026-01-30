print('=' * 30)
print('       BANCO CEV     ')
print('=' * 30)

valor = int(input('Qual valor voce quer sacar? R$'))
total = valor 
cedula = 50 
tot = 0
while True:
    if total >= cedula:
        total -= cedula
        tot += 1 
    else: 
        if tot > 0:
            print(f'O total de {tot} cedulas de R${cedula}')
        if cedula == 50: 
            cedula = 20
        elif cedula == 20:   
            cedula = 10
        elif cedula == 10: 
            cedula = 1
        tot = 0 
        if total == 0:
            break

print('=' * 30 )
print('         Volte sempre')
print('=' * 30 )
