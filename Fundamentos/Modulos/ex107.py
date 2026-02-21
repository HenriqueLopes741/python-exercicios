from Fundamentos.Modulos.funções import aumentar, metade, dobro
a = int(input("Digite o preço do produto: R$"))
print('-=' * 20)
print(f'A metade de R${a} é R${metade(a)} Reais')
print(f'O dobro de R${a} é R${dobro(a)} reais')
print(f'Aumentando 10%, temos R${aumentar(a)} reais ')
print('-=' * 20)
