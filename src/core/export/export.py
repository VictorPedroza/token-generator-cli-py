import os
from datetime import datetime
from typing import List, Optional


class TokenExporter:
    def __init__(self, output_dir: str = "exports"):
        """ Inicializa o exportador """
        self.output_dir = output_dir
        self._create_output_dir()
    
    def _create_output_dir(self) -> None:
        """Cria o diretório de saída se não existir"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
    def _generate_file_name(self, extension: str) -> str:
        """ Gera um nome único para o arquivo """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"tokens_{timestamp}.{extension}"
        return os.path.join(self.output_dir, file_name)
    
    def export_txt(self, tokens: List[str], header: Optional[str] = None) -> str:
        """ Exporta o Token para TXT """
        file_path = self._generate_file_name("txt")
        
        with open(file_path, 'w', encoding='utf-8') as file:
            if header:
                file.write(f"{header}\n")
            else: 
                file.write(f"Tokens gerados em {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            
            file.write("=" * 50 + "\n\n")

            for i, token in enumerate(tokens, 1):
                file.write(f"{i:4d}. {token}\n")  # Corrigido: faltava o \n

            file.write("\n" + "=" * 50 + "\n")
            file.write(f"Total de tokens: {len(tokens)}")

        return file_path