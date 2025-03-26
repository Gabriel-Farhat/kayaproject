# Projeto: STeste para o programador júnior em Django

## Descrição
Este projeto foi proposto como um teste para replicar uma página funcional de perfis de médicos. A aplicação foi construída utilizando **Django**, **Tailwind CSS** e um ambiente virtual Python (**.venv**).

## Tecnologias Utilizadas
- **Django**: Framework web em Python para construção da aplicação.
- **Tailwind CSS**: Framework CSS para estilização responsiva e moderna.
- **Ambiente Virtual (.venv)**: Gerenciamento de dependências do Python.

## Instalação e Configuração
Siga os passos abaixo para instalar e executar o projeto localmente:

### 1. Clonar o Repositório
```bash
    git clone https://github.com/Gabriel-Farhat/kayaproject
    cd kayaproject
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate     # Windows
```

### 3. Instalar Dependências
```bash
    pip install -r requirements.txt
```

### 5. Executar o Servidor
```bash
    python manage.py runserver
```

O projeto estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura do Projeto
```
meu_projeto/
├── my_app/                 # Aplicativo principal
│   ├── templates/components/  # Templates de perfis de médicos
│   ├── views.py            # Lógica das rotas
│   ├── urls.py             # Configuração das rotas
├── static/                 # Arquivos CSS e JavaScript
├── .venv/                  # Ambiente virtual Python
├── manage.py               # Arquivo principal do Django
└── requirements.txt        # Dependências do projeto
```

## Contato
Caso tenha alguma dúvida ou sugestão, entre em contato pelo e-mail: **farhatgabrielr@gmail.com**.

---
**Autor:** Gabriel Farhat | **Data:** 26/03/2025

