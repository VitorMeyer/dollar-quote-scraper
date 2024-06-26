# Projeto de Web Scraping - Cotação do Dólar

Este projeto realiza web scraping no Google para obter a cotação do dólar.

## Pré-requisitos

- Python 3.6 ou superior
- Pip (gerenciador de pacotes do Python)

## Configuração do Ambiente

### 1. Clonar o Repositório

Clone o repositório do GitHub para sua máquina local:
```bash

cd dollar-quote-scraper
````
### 2. Criar um Ambiente Virtual
Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv

```
### 3. Ativar o Ambiente Virtual
Ative o ambiente virtual:

No Windows:
```bash

venv\Scripts\activate
```
No macOS/Linux:
```
bash

source venv/bin/activate
```
### 4. Instalar as Dependências
Instale as dependências listadas no arquivo requirements.txt:

```bash

pip install -r requirements.txt
```
### 5. Executar o Script
Execute o script main.py para obter a cotação do dólar:

```bash

python main.py
```
### Estrutura do Projeto
```plaintext
dolar_scraping/
├── venv/               # Ambiente virtual
├── main.py          # Script principal de web scraping
├── requirements.txt    # Arquivo de dependências
├── README.md           # Documentação do projeto
└── .gitignore          # Arquivo para ignorar arquivos/pastas no git
