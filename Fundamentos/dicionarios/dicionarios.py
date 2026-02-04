
pessoa = {
    "nome": "Henrique",
    "idade": 20,
    "curso": "Ciência da Computação"
}

# Percorrendo um dicionário

#🔹 Só as chaves
for chave in pessoa:
    print(chave)

#🔹 Só os valores
for valor in pessoa.values():
    print(valor)

#🔹 Chave e valor juntos
for chave, valor in pessoa.items():
    print(chave, "=", valor)

pessoa.keys()     # todas as chaves
pessoa.values()   # todos os valores
pessoa.items()    # chave e valor
len(pessoa)       # quantidade de elementos


aluno = {
    "nome": "Henrique",
    "notas": [8.5, 7.0, 9.0],
    "aprovado": True
}

media = sum(aluno["notas"]) / len(aluno["notas"])

print(f"Aluno: {aluno['nome']}")
print(f"Média: {media}")
