from datetime import datetime
from typing import List, Optional

class TokenStorage:
    """ Gerencia o armazenamento de tokens """
    def __init__(self):
        """ Inicializa o armazenamento vazio """
        self._tokens = [str]  # Corrigido: era [str] (lista com um elemento str), agora é [] (lista vazia)
        self._metadata = {
            'Criado_em': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Ultima_atualizacao': None
        }

    def add_token(self, token: str) -> None:
        """ Adiciona um único token ao armazenamento """
        self._tokens.append(token)
        self._uptade_metadata()

    def add_tokens(self, tokens: List[str]) -> None:
        """ Adiciona multiplos tokens ao armazenamento """
        self._tokens.extend(tokens)
        self._uptade_metadata()

    def list_tokens(self) -> List[str]:
        """ Retorna os tokens armazenados """
        return self._tokens.copy()
    
    def clear_tokens(self) -> None:
        """ Limpa todos os tokens """
        self._tokens.clear()
        self._uptade_metadata()

    def get_token_by_index(self, index: int) -> Optional[str]:
        """ Retorna um token especifico """
        if 0 <= index < len(self._tokens):
            return self._tokens[index]
        return None

    def _uptade_metadata(self) -> None:
        """ Atualiza os metadados do armazenamento """
        self._metadata['Ultima_atualizacao'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_metadata(self) -> dict:
        """ Retorna os metadados do armazenamento """
        return {
            **self._metadata,
            'total_tokens': self.count_tokens()
        }

    def count_tokens(self) -> int:
        """ Retorna a quantidade de token """
        return len(self._tokens)