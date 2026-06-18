from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import os

console = Console()

def saudacao():

     """
     Terminal inicial do projeto Orion
     """

     console.print(
            Align.center(
            Panel
            ("Orion.AI 🥖", width=80, style="bold red")))
        

     print()
     print()
     print()
     print()

saudacao()

console = Console()

class Orion:

    def __init__(self):
        self.versao = "Orion v0.1.1"

    def help(self):
        console.print("\n[bold cyan]Comandos disponíveis:[/bold cyan]")
        console.print("[bold green]help[/bold green]    - Exibe essa mensagem")
        console.print("[bold green]version[/bold green] - Exibe a versão da Orion")
        console.print("[bold green]limpar[/bold green]  - Limpa a tela")
        console.print("[bold green]exit[/bold green]    - Encerra a sessão")

    def version(self):
        console.print(f"[bold red]Versão:[/bold red] {self.versao}")

    def limpar(self):
        os.system("cls" if os.name == "nt" else "clear")

    def run(self):

        while True:

            inserir = input("Orion > ").strip().lower()

            if inserir == "help":
                self.help()

            elif inserir == "version":
                self.version()

            elif inserir == "limpar":
                self.limpar()

            elif inserir == "exit":
                console.print("[bold red]Encerrando Orion...[/bold red]")
                break

            else:
                console.print(
                    "[bold red]Comando desconhecido. Digite 'help' para mais informações.[/bold red]"
                )