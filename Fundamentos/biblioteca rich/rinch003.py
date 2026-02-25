from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", style="red")
tabela.add_column("Preço", style="blue")

tabela.add_row("Lapis", "R$1,50")
tabela.add_row("Borracha", "R$5,00")


print(tabela)