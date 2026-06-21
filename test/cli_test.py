from rich.console import Console
from rich.panel import Panel
from rich.align import Align

from translate_test import Translate

console = Console()


def saudacao():

    console.print(
        Align.center(
            Panel(
                "Orion.AI 🥖 v0.1.2",
                width=50,
                style="bold red"
            )
        )
    )

    print()


class Orion:

    def __init__(self):

        self.translate = Translate()

    def run(self):

        while True:

            comando = input("Orion > ").strip().lower()

            if comando == "exit":
                console.print(
                    "[bold red]Encerrando Orion...[/bold red]"
                )
                break

            self.translate.execute(comando)