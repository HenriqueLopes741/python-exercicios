from rich import print
from rich.panel import Panel
 
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        caixa = Panel(f"{self.nome} \n R${self.preco:,.2f}", title="Produto", title_align="center", width=30)
        print(caixa)

p1 = Produto("Iphone 17 Pro Max", 2500085)
p1.etiqueta()

p2 = Produto("Notebook Gamer", 8000)