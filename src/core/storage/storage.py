from datetime import datetime

class TokenStorage:
    """ Gerencia o armazenamento de tokens """
    def __init__(self):
        """ Inicializa o armazenamento vazio """
        self._tokens = [str]
        self._metadata = {
            'Criado_em': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Ultima_atualizacao': None
        }

    def add_token(self, token):
        """ Adiciona um único token ao armazenamento """
        self._tokens.append(token)
        self._uptade_metadata()

    def add_tokens(self, tokens):
        """ Adiciona multiplos tokens ao armazenamento """
        self._tokens.extend(tokens)
        self._uptade_metadata()

    def list_tokens(self):
        """ Retorna os tokens armazenados """
        return self._tokens.copy()
    
    def clear_tokens(self):
        """ Limpa todos os tokens """
        self._tokens.clear()
        self._uptade_metadata()

    def get_token_by_index(self, index):
        """ Retorna um token especifico """
        if 0 <= index < len(self._tokens):
            return self._tokens[index];
        return None;

    def _uptade_metadata(self):
        """ Retorna os metadados do armazenamento """
        self._metadata['Ultima_atualizacao'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_metadata(self):
        """ Retortna os metadados do armazenamento """
        return {
            **self._metadata,
            'total_tokens': self.count_tokens()
        }

    def count_tokens(self):
        """ Retorna a quantidade de token """
        return len(self._tokens)
