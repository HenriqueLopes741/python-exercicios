nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))

media = (nota1 + nota2) / 2 

if media >= 7:
    print(f'Sua media foi {media} , Voce Passou')
elif media <= 5:
    print(f'Sua media foi {media} , Voce reprovou')
else:
    print(f'A sua media foi {media}, Voce ficou de recuperação')
