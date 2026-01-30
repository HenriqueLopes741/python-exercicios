numeros = []

for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)

numeros.insert(6, 6 )

#del numeros[] 
#numeros.remove(3)
valores = list(range(4,11))
#print(valores)

print("Lista:", numeros)
print("Tamanho: ", len(numeros))
print("Organizado:", sorted(numeros))
print("Maior:", max(numeros))
print("Menor:", min(numeros))
print("Soma:", sum(numeros))
