from rich.console import Console
import os

console = Console()


class Commands:

    def __init__(self):

        self.versao = "Orion v0.1.2"

    def help(self):

        console.print(
            "\n[bold cyan]Comandos disponíveis:[/bold cyan]"
        )

        console.print(
            "[bold green]help[/bold green] - Exibe esta mensagem"
        )

        console.print(
            "[bold green]version[/bold green] - Mostra a versão"
        )

        console.print(
            "[bold green]limpar[/bold green] - Limpa o terminal"
        )

        console.print(
            "[bold green]exit[/bold green] - Encerra a aplicação"
        )

    def version(self):

        console.print(
            f"[bold red]Versão:[/bold red] {self.versao}"
        )

    def limpar(self):

        os.system(
            "cls" if os.name == "nt" else "clear"
        )