aluno = {}

aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

print('-=' * 30)

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7 :
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'


for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')