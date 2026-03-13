import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich import box  

class TokenCli:
    def __init__(self):
        """ Inicializa o cli com todos os componentes """
        self.console = Console()

    def start(self):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else clear)
                self.header()
                self.menu()
        
        except KeyboardInterrupt:
            self.console.print("\n\n[bold cyan]👋 Até logo![/bold cyan]")
            sys.exit(0)

    def header(self):
        """" Exibe o cabeçalho do programa """
        header = Panel(
            "[bold cyan]🔑 GERADOR DE TOKENS[/bold cyan]\n"
            "[italic]Gere e gerencie tokens - By Victor Pedroza[/italic]",
            box=box.DOUBLE,
        )
        self.console.print(header)

    def menu(self):
        """ Exibe o Menu Principal """
        menu = Panel(
            "[bold yellow]1.[/bold yellow] Gerar token único\n"
            "[bold yellow]2.[/bold yellow] Gerar múltiplos tokens\n"
            "[bold yellow]3.[/bold yellow] Listar tokens gerados\n"
            "[bold yellow]4.[/bold yellow] Limpar tokens\n"
            "[bold yellow]5.[/bold yellow] Exportar tokens\n"
            "[bold red]6.[/bold red] Sair",
            title="[bold]MENU PRINCIPAL[/bold]",
            box=box.ROUNDED,
            width=50
        )
        self.console.print(menu)