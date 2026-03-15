import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich import box  
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from service.token import TokenGenerator
from core.storage.storage import TokenStorage
from core.export.export import TokenExporter


class TokenCli:
    def __init__(self):
        """ Inicializa o cli com todos os componentes """
        self.console = Console()
        self.token = TokenGenerator()
        self.storage = TokenStorage()
        self.exporter = TokenExporter()

    def start(self):
        """Loop principal do programa"""
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.header()
                self.status()
                self.menu()

                try:
                    option = IntPrompt.ask("\n[bold]Escolha uma opção:[/bold]", choices=['1','2','3','4','5','6'])

                    if option == 1:
                        self.generate_token()
                    elif option == 2:
                        self.generate_tokens()
                    elif option == 3:
                        self.list_tokens()
                    elif option == 4:
                        self.clear_tokens()
                    elif option == 5:
                        self.export_tokens()
                    elif option == 6:
                        self.console.print("\n[bold cyan]👋 Até logo![/bold cyan]")
                        break

                    if option in [1, 2, 3, 4, 5]:
                        self.console.print("\n[dim]Pressione Enter para continuar...[/dim]", end="")
                        input()
                
                except KeyboardInterrupt:
                    self.console.print("\n[yellow]Operação Cancelada[/yellow]")
                    continue
        
        except KeyboardInterrupt:
            self.console.print("\n\n[bold cyan]👋 Até logo![/bold cyan]")
            sys.exit(0)

    def header(self):
        """Exibe o cabeçalho do programa"""
        header = Panel(
            "[bold cyan]🔑 GERADOR DE TOKENS[/bold cyan]\n"
            "[italic]Gere e gerencie tokens - By Victor Pedroza[/italic]",
            box=box.DOUBLE,
        )
        self.console.print(header)

    def menu(self):
        """Exibe o Menu Principal"""
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
        """Exibe o Status (Quantidade de Tokens)"""
        total = self.storage.count_tokens()
        status = f"[bold blue]📊 Tokens na sessão: {total}[/bold blue]"
        self.console.print(Panel(status, box=box.SQUARE))

    def choose_token_type(self):
        """Menu para escolha do tipo de token"""
        self.console.print("\n[bold]Tipo do token:[/bold]")
        self.console.print("1. [green]Letras[/green] (a-z, A-Z)")
        self.console.print("2. [blue]Números[/blue] (0-9)")
        self.console.print("3. [yellow]Símbolos[/yellow] (!@#$%...)")
        self.console.print("4. [magenta]Alfanumérico[/magenta] (letras + números)")

        while True:
            try:
                type_choice = IntPrompt.ask("[bold]Escolha[/bold]", choices=["1", "2", "3", "4"])
                return type_choice
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Operação cancelada[/yellow]")
                return None
            
    def generate_token(self):
        """Fluxo para gerar token único"""
        self.console.rule("[bold]Gerar Token Único[/bold]")

        type_choice = self.choose_token_type()
        if type_choice is None:
            return

        size = IntPrompt.ask("[bold]Tamanho do Token[/bold]", default=8)

        with self.console.status("[bold green]Gerando token..."):
            token = self.token.gerar_token(type_choice, size)
            self.storage.add_token(token)

        self.console.print(f"\n[bold green]✅ Token gerado:[/bold green] [cyan]{token}[/cyan]")
        self.console.print(f"[dim]Tipo: {self.token.obter_nome_tipo(type_choice)} | Tamanho: {size}[/dim]")

    def generate_tokens(self):
        """Fluxo para gerar múltiplos tokens"""
        self.console.rule("[bold]Gerar múltiplos tokens[/bold]")

        qtd = IntPrompt.ask("[bold]Quantidade de Tokens[/bold]", default=5)
        type_choice = self.choose_token_type()
        if type_choice is None:
            return
        
        size = IntPrompt.ask("[bold]Tamanho de cada token:[/bold]", default=8)

        with self.console.status(f"[bold green]Gerando {qtd} tokens..."):
            tokens = self.token.gerar_multiplos_tokens(qtd, type_choice, size)
            self.storage.add_tokens(tokens)

        self.console.print(f"\n[bold green]✅ {qtd} tokens gerados com sucesso![/bold green]")
        
        # Preview dos primeiros tokens
        self.console.print("\n[bold]Preview:[/bold]")
        for i, token in enumerate(tokens[:5], 1):
            self.console.print(f"  {i}. [cyan]{token}[/cyan]")
        
        if qtd > 5:
            self.console.print(f"  ... e mais {qtd - 5} tokens")

    def list_tokens(self):
        """Lista de tokens armazenados"""
        self.console.rule("[bold]Tokens Gerados[/bold]")

        tokens = self.storage.list_tokens()
        metadata = self.storage.get_metadata()

        if not tokens:
            self.console.print("[yellow]⚠️ Nenhum token gerado[/yellow]")
            return

        table = Table(title=f"Tokens na Sessão (Total: {len(tokens)})", box=box.ROUNDED)
        table.add_column("#", style="cyan", justify="right")
        table.add_column("Token", style="green")

        for i, token in enumerate(tokens, 1):
            table.add_row(str(i), token)

        self.console.print(table)

        self.console.print(f"\n[dim]Sessão criada em: {metadata['Criado_em']}[/dim]")
        if metadata['Ultima_atualizacao']:
            self.console.print(f"[dim]Última atualização: {metadata['Ultima_atualizacao']}[/dim]")

    def clear_tokens(self):
        """Limpa todos os tokens da memória"""
        self.console.rule("[bold]Limpar Tokens[/bold]")

        total = self.storage.count_tokens()
        if total == 0:
            self.console.print("[yellow]⚠️ Não há tokens para limpar[/yellow]")
            return
            
        confirm = Prompt.ask(
            f"[red]Tem certeza que deseja limpar {total} tokens?[/red] (s/N)", 
            choices=["s","S","n","N"], 
            default="n"
        )

        if confirm.lower() == "s":
            self.storage.clear_tokens()
            self.console.print("[green]✅ Todos os tokens foram removidos![/green]")
        else:
            self.console.print("[yellow]Operação cancelada[/yellow]")

    def export_tokens(self):
        """Exporta os tokens para arquivo"""
        self.console.rule("[bold]Exportar Tokens[/bold]")

        tokens = self.storage.list_tokens()
        
        if not tokens:
            self.console.print("[yellow]⚠️ Não há tokens para exportar.[/yellow]")
            return
            
        self.console.print(f"📁 Exportando [bold]{len(tokens)}[/bold] tokens...")
        self.console.print("1. [blue]TXT[/blue] - Arquivo texto simples")
        self.console.print("2. [red]PDF[/red] - Documento formatado")

        export_format = Prompt.ask("[bold]Escolha o Formato[/bold]", choices=["1", "2"])

        with self.console.status("[bold green]Exportando...[/bold green]"):
            if export_format == "1":
                path = self.exporter.export_txt(tokens, None)  # Adicionado o parâmetro header
            # else:
            #     path = self.exporter.export_pdf(tokens)  # Precisa implementar export_pdf

        self.console.print(f"\n[bold green]✅ Tokens exportados com sucesso![/bold green]")
        self.console.print(f"[cyan]📄 Arquivo: {path}[/cyan]")