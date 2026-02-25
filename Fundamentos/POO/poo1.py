class classe:
    def __init__(self, n = "Vazio", i= 0):
        self.nome = n
        self.idade = i
        self.estuda = ""
    
    def aniversario(self):
        self.idade = self.idade + 1

    def __str__(self):
        return f'O seu nome é {self.nome} tem {self.idade} anos e estuda {self.estuda}'
    
p1 = classe("maria", 17)
p1.estuda = "Faculdade - IESB"
print(p1)

p2 = classe("Mauro", 55)
print(p2)

p3 = classe()
print(p3)


print(p1)