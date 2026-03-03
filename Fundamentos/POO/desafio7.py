from rich.console import Console

class Caneta:
    def __init__(self, cor, tampada=True):
        self.cor = cor
        self.tampada = tampada
        self.console = Console()

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            self.console.print("A caneta está tampada!", style="bold red")
        else:
            self.console.print(texto, style=self.cor, end="")

    def quebrar_linha(self, n):
        self.console.print("\n" * n)

c1 = Caneta("blue")
c2 = Caneta("red")
c3 = Caneta("green")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebrar_linha(3)

c2.escrever("Como você vai???")
c2.quebrar_linha(3)