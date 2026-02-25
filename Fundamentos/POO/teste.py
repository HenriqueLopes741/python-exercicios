#declaração da classe
class Henrique:
    def __init__(self): #MEtodo Construtor
        #Atributos
        self.nome = ""
        self.idade = 0

    #Metodos de Instancia
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Louco e tem {self.idade} anos de idade."


#declaração dos objetos

h1 = Henrique()
h1.nome = "Maria"
h1.idade = 17
h1.aniversario()
print(h1.mensagem())

h2 = Henrique()
h2.nome = "Henrique"
h2.idade = 18
h2.aniversario()
print(h2.mensagem())