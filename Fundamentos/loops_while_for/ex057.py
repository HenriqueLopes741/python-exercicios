s = str(input('Informe seu sexo: [M/F] ')).strip().upper()

while s not in 'MF':
    s = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()

print(f'Sexo {s} registrado com sucesso')