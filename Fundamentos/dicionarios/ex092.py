from datetime import datetime

informações = dict()

informações['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
informações['Idade'] = datetime.now().year - nasc
informações['carteira'] = int(input('Carteira de trabalho (0 nao tem): '))

if informações['carteira'] != 0:
    informações['contrato'] = int(input('Ano de contrato: '))
    informações['salario'] = float(input('Salario: R$'))
    informações['aposentadoria'] = informações['Idade'] + ((informações['contrato'] + 35) - datetime.now().year)
print('-=' * 30)

for k, v in informações.items():
    print(f'  - {k} tem o valor {v}')
    



