"""
Módulo responsável pela exportação de tokens para arquivos
"""

import os
from datetime import datetime
from typing import List, Optional
from fpdf import FPDF


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
                file.write(f"{i:4d}. {token}\n")

            file.write("\n" + "=" * 50 + "\n")
            file.write(f"Total de tokens: {len(tokens)}")

        return file_path
    
    def export_pdf(self, tokens: List[str], header: Optional[str] = None) -> str:
        """ Exporta os tokens para PDF com suporte a Unicode """
        file_path = self._generate_file_name("pdf")
        
        # Cria o PDF com suporte a Unicode
        pdf = FPDF()
        pdf.add_page()
        
        # Tenta adicionar fontes Unicode (se disponíveis no sistema)
        # Fallback para fontes padrão se não encontrar
        
        # Título (sem emojis para evitar problemas)
        pdf.set_font("Arial", "B", 16)
        pdf.set_text_color(0, 51, 102)  # Azul escuro
        pdf.cell(190, 15, "GERADOR DE TOKENS", ln=True, align="C")
        pdf.ln(5)
        
        # Linha decorativa
        pdf.set_draw_color(0, 102, 204)  # Azul
        pdf.set_line_width(0.5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(10)
        
        # Data/Hora
        pdf.set_font("Arial", "I", 10)
        pdf.set_text_color(100, 100, 100)  # Cinza
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        pdf.cell(190, 8, f"Gerado em: {data}", ln=True, align="R")
        pdf.ln(5)
        
        # Cabeçalho personalizado (se fornecido)
        if header:
            pdf.set_font("Arial", "B", 12)
            pdf.set_text_color(0, 0, 0)  # Preto
            # Remove emojis do header se houver
            header_limpo = header.encode('ascii', 'ignore').decode('ascii')
            pdf.multi_cell(190, 8, header_limpo, align="C")
            pdf.ln(5)
        
        # Total de tokens
        pdf.set_font("Arial", "B", 11)
        pdf.set_text_color(0, 102, 204)  # Azul
        pdf.cell(190, 8, f"Total de tokens: {len(tokens)}", ln=True, align="L")
        pdf.ln(5)
        
        # Linha separadora
        pdf.set_draw_color(200, 200, 200)  # Cinza claro
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        # Tokens
        pdf.set_font("Courier", "", 10)
        pdf.set_text_color(0, 0, 0)  # Preto
        
        for i, token in enumerate(tokens, 1):
            # Verifica se precisa de nova página
            if pdf.get_y() > 250:  # Altura máxima da página
                pdf.add_page()
                # Restaura as configurações na nova página
                pdf.set_font("Courier", "", 10)
                pdf.set_text_color(0, 0, 0)
            
            # Formata a linha com número e token
            # Remove caracteres não latinos se necessário
            try:
                linha = f"{i:4d}. {token}"
                # Tenta escrever normalmente
                pdf.cell(190, 6, linha, ln=True)
            except:
                # Se falhar, tenta remover caracteres problemáticos
                linha_limpa = token.encode('latin-1', 'ignore').decode('latin-1')
                linha = f"{i:4d}. {linha_limpa}"
                pdf.cell(190, 6, linha, ln=True)
        
        # Linha final
        pdf.ln(5)
        pdf.set_draw_color(200, 200, 200)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        # Resumo
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(0, 102, 204)
        pdf.cell(190, 8, f"Documento gerado em: {data}", ln=True, align="C")
        
        # Salva o PDF
        pdf.output(file_path)
        
        return file_path