peso = float(input('Qual é seu peso (KG): '))
altura = float(input('Qual é a sua altura (m): '))

a = altura * altura
imc = peso / a

if imc < 18.5:
    print(f'O seu IMC é de {imc:.2f} ')
    print('Você esta abaixo do peso')
elif imc > 18.5 and imc < 25:
    print(f'O seu IMC é de {imc:.2f} ')
    print('Você esta no peso ideal')
elif imc > 25 and imc < 30:
    print(f'O seu IMC é de {imc:.2f} ')
    print('Você esta no com sobrepeso')
elif imc > 30 and imc < 40:
    print(f'O seu IMC é de {imc:.2f} ')
    print('Você esta no com obesidade')
else:
    print(f'Seu IMC é de {imc}')
    print('Voce esta com OBESIDADE MORBIDA')
    print('PROCURE UM MEDICO URGENTE')
