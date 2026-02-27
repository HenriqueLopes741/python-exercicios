from rich import print
from rich.table import Table


class Livro:
    def __init__(self, titulo, total):
        self.titulo = titulo
        self.total = total
        self.pagina_atual = 1

        print(f"[blue]Você abriu o livro '[red]{self.titulo}[/red]'[/blue]")
        self.status()

    def avancar(self, paginas):
        self.pagina_atual += paginas

        if self.pagina_atual >= self.total:
            self.pagina_atual = self.total
            print("[bold red]Você chegou ao final do livro![/bold red]")

        self.status()

    def status(self):
        progresso = (self.pagina_atual / self.total) * 100

        table = Table(title="📘 Status do Livro", show_lines=True)

        table.add_column("Título", style="cyan", justify="center")
        table.add_column("Página Atual", style="yellow", justify="center")
        table.add_column("Total de Páginas", style="green", justify="center")
        table.add_column("Progresso", style="magenta", justify="center")

        table.add_row(
            self.titulo,
            str(self.pagina_atual),
            str(self.total),
            f"{progresso:.2f}%"
        )

        print(table)

livro1 = Livro("Python para Iniciantes", 250)

livro1 = Livro("Python para Iniciantes", 250)

livro1.avancar(10)
livro1.avancar(50)
livro1.avancar(300)