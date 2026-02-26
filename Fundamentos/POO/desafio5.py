from rich import print

class Livro:
    def __init__(self, titulo, total):
        self.titulo = titulo
        self.total = total
        self.pagina_atual = 1

        print(
            f"[blue]Você acabou de abrir o livro '[red]{self.titulo}[/red]' "
            f"que tem [green]{self.total} páginas[/green] no total. "
            f"Você agora está na página [yellow]{self.pagina_atual}[/yellow].[/blue]"
        )

    def avancar(self, paginas):
        self.pagina_atual += paginas

        if self.pagina_atual > self.total:
            self.pagina_atual = self.total
            print("[red]Você chegou ao final do livro![/red]")
        else:
            print(f"[green]Você avançou para a página {self.pagina_atual}[/green]")

livro1 = Livro("Python para Iniciantes", 250)

livro1.avancar(10)
livro1.avancar(50)
livro1.avancar(300)