from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, nome, quantidade, ):
        self.nome = nome
        self.quantidade = quantidade
        self.analisar()
        
    def analisar(self):
        self.kg = self.quantidade * 0.40
        self.tot = self.kg * 82.40
        self.divisao = self.tot / self.quantidade
    
    def mensagem(self):
        painel = Panel(f"Analisando [green]Churras dos Amigos[/green] com [blue]{self.divisao} convidados[/blue]\n"
                       f"Cada Participante Comera 0.4Kg e cada Kg custa R$82.40\n"
                       f"Recomendo [blue]comprar {self.kg} de carne\n"
                       f"O custo total será de [green]R${self.tot:.2f}[/green]\n"
                       f"Cada pessoa pagará [yellow]R${self.divisao:.2f}[/yellow] para participar.", title="Churras dos Amigos")
        print(painel)


p1 = Churrasco("Churras dos amigos", 15)
print(p1.mensagem())

