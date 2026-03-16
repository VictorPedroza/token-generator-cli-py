# 🔐 Token Generator CLI

Um gerador de tokens via terminal para criar, armazenar temporariamente e exportar tokens em diferentes formatos como TXT e PDF.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-orange)
![Rich](https://img.shields.io/badge/rich-14.3.3-yellow)
![FPDF](https://img.shields.io/badge/fpdf-1.7.2-green)

## 📸 Screenshots



## ✨ Funcionalidades

- ✅ **Geração de tokens**: Crie tokens seguros com comprimento personalizável
- ✅ **Armazenamento temporário**: Tokens salvos em cache para acesso rápido
- ✅ **Exportação para PDF**: Gere documentos PDF profissionais com fpdf
- ✅ **Exportação para TXT**: Exporte tokens em formato texto simples
- ✅ **Interface rica no terminal**: Outputs coloridos e formatados com Rich
- ✅ **Syntax highlighting**: Código e tokens destacados com Pygments
- ✅ **Markdown 6**: Renderização de markdown nos relatórios
- ✅ **CLI intuitiva**: Interface de linha de comando simples e direta
- ✅ **Gerenciamento de tokens**: Visualize, liste e remova tokens armazenados
- ✅ **Validação de entrada**: Tratamento de erros e validações robustas

## 🚀 Tecnologias Utilizadas

- **Python 3.7+**: Linguagem de programação principal
- **Rich 14.3.3**: Interface de terminal elegante e formatação
- **FPDF 1.7.2**: Geração de arquivos PDF

## 📋 Pré-requisitos

- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/VictorPedroza/token-generator-cli-py.git
cd token-generator-cli-py
```

2. **Crie o Ambiente Virtual (Recomendado)**
```
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências**
```
pip install -r requirements.txt
```
- Verifique as dependências [AQUI](requirements.txt)

4. **Execute o Projeto**
```
python src/main.py
```

## 📁 Estrutura do Projeto
```
token-generator-cli-py/
│
├── src/                            # Diretório principal
│   ├── core/                       # Núcleo do sistema
│   │   ├── cli/                     
│   │   │   ├── token_cli.py        # CLI principal (com Rich)
│   │   ├── export/                  
│   │   │   ├── export.py           # Exportação TXT/PDF com FPDF
│   │   └── storage/                  
│   │       ├── storage.py          # Gerenciamento de cache
│   └── service/                    # Camada de serviço
│       ├── token.py                # Lógica de geração de tokens
├── main.py                         # Arquivo principal do Projeto
├── .gitignore                      # Arquivos ignorados pelo Git
├── LICENSE                         # Licença do projeto
├── README.md                       # Documentação
└── requirements.txt                # Dependências do projeto
```

## 🎯 Como Usar

Ao executar o programa, você verá o menu principal com as seguintes opções:
Opção	Descrição	Ação:

1. **Gerar token único:** Gera um único token com comprimento padrão ou personalizado
2. **Gerar múltiplos tokens:** Gera vários tokens de uma só vez (escolha a quantidade)
3. **Listar tokens gerados:** Exibe todos os tokens armazenados na sessão atual
4. **Limpar tokens:** Remove todos os tokens da sessão atual
5. **Exportar tokens:** Exporta os tokens para TXT ou PDF
6. **Sair:** Encerra o programa


## 📦 Formatos de Exportação
### TXT
* Arquivo texto simples com todos os tokens
* Inclui cabeçalho com data e hora
* Tokens listados com seus respectivos IDs

### PDF
* Documento profissional gerado com FPDF
* Cabeçalho personalizado "Token Generator - By Victor Pedroza"
* Tabela com todos os tokens e metadados
* Data e hora da exportação
* Número total de tokens exportados

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENCE](LICENSE) para mais detalhes.
