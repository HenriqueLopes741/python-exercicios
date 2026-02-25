class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f"O meu nome é {self.nome} trabalho no setor {self.setor} e atualmente atuo no cargo de {self.cargo}"


p1 = Funcionario("Henrique", "Dev", "Automação de processos")
print(p1)

p2 = Funcionario("Pedro", "TI", "Programador")
print(p2)