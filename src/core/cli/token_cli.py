import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich import box  
from rich.prompt import Prompt, IntPrompt

class TokenCli:
    def __init__(self):
        """ Inicializa o cli com todos os componentes """
        self.console = Console()

    def start(self):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else clear)
                self.header()
                self.status()
                self.menu()

                try:
                    option = IntPrompt.ask("\n[bold]Escolha uma opção:[bold]", choices=['1','2','3','4','5','6'])

                    if option == 1:
                        print("Opção: Gerar um token")
                    elif option == 6:
                        self.console.print("\n[bold cyan]👋 Até logo![/bold cyan]")
                        break

                    if option in [1,2,3,4,5,6]:
                        self.console.print("\n[dim]Pressione Enter para continuar...[/dim]", end="")
                        input()
                
                except KeyboardInterrupt:
                    self.console.print("\n[yellow] Operação Cancelada[/yellow]")
                    continue
        
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
            "[bold blue]1.[/bold blue] Gerar token único\n"
            "[bold blue]2.[/bold blue] Gerar múltiplos tokens\n"
            "[bold blue]3.[/bold blue] Listar tokens gerados\n"
            "[bold blue]4.[/bold blue] Limpar tokens\n"
            "[bold blue]5.[/bold blue] Exportar tokens\n"
            "[bold red]6.[/bold red] Sair",
            title="[bold]MENU PRINCIPAL[/bold]",
            box=box.ROUNDED,
            width=50
        )
        self.console.print(menu)

    def status(self):
        """ Exibe o Satus (Quantidade de Tokens) """
        status = f"[bold blue]📊 Tokens na sessão: 2[/bold blue]"
        self.console.print(Panel(status, box=box.SQUARE))