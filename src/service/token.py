import secrets
import string

class TokenGenerator:
    """Classe responsável por gerar tokens de diferentes tipos usando secrets"""
    
    LETRAS = string.ascii_letters
    NUMEROS = string.digits
    SIMBOLOS = string.punctuation
    ALFANUMERICO = string.ascii_letters + string.digits
    
    @staticmethod
    def gerar_token(tipo: int, tamanho: int) -> str:
        """
        Gera um único token baseado no tipo e tamanho especificados
        
        Args:
            tipo (int): 1-Letras, 2-Números, 3-Símbolos, 4-Alfanumérico
            tamanho (int): Tamanho do token a ser gerado
            
        Returns:
            str: Token gerado
        """
        if tipo == 1:
            caracteres = TokenGenerator.LETRAS
        elif tipo == 2:
            caracteres = TokenGenerator.NUMEROS
        elif tipo == 3:
            caracteres = TokenGenerator.SIMBOLOS
        elif tipo == 4:
            caracteres = TokenGenerator.ALFANUMERICO
        else:
            raise ValueError("Tipo de token inválido")
        
        return ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    @staticmethod
    def gerar_multiplos_tokens(quantidade: int, tipo: int, tamanho: int) -> list:
        """
        Gera múltiplos tokens
        
        Args:
            quantidade (int): Número de tokens a serem gerados
            tipo (int): Tipo do token (1-4)
            tamanho (int): Tamanho de cada token
            
        Returns:
            list: Lista de tokens gerados
        """
        tokens = []
        for _ in range(quantidade):
            token = TokenGenerator.gerar_token(tipo, tamanho)
            tokens.append(token)
        return tokens
    
    @staticmethod
    def obter_nome_tipo(tipo: int) -> str:
        """Retorna o nome descritivo do tipo de token"""
        tipos = {
            1: "Letras",
            2: "Números",
            3: "Símbolos",
            4: "Alfanumérico"
        }
        return tipos.get(tipo, "Desconhecido")