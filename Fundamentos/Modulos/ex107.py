from Fundamentos.Modulos.funções import aumentar, metade, dobro
a = int(input("Digite o preço: R$"))
print('-=' * 20)
print(f'A metade de R${a} é R${metade(a)}')
print(f'O dobro de R${a} é R${dobro(a)}')
print(f'Aumentando 10%, temos R${aumentar(a)}')
print('-=' * 20)
