# Desafio Tecnico AutoClipper

# YouTube Channel Video Extractor API

API desenvolvida em Python com Flask para extrair informações de vídeos de um canal do YouTube com base em tags fornecidas.

## Descrição

A aplicação recebe o nome de um canal do YouTube e uma lista de tags. Ela busca os vídeos do canal, filtra aqueles que contêm as tags informadas e retorna os dados em formato JSON.

As informações retornadas incluem:

* Título do vídeo
* Descrição
* Tags
* Data de publicação
* Número de visualizações
* Número de likes
* Número de comentários
* Duração

---

## Tecnologias Utilizadas

* Python
* Flask
* Requests
* YouTube Data API v3
* SQLite (opcional, caso esteja utilizando banco)
* python-dotenv

---

## Configuração do Ambiente

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-projeto>
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração da API do YouTube

1. Criar um projeto no Google Cloud.
2. Ativar a YouTube Data API v3.
3. Gerar uma API Key.
4. Criar um arquivo `.env` na raiz do projeto:

```
YOUTUBE_API_KEY=sua_chave_aqui
```

5. Certificar-se de que o projeto está carregando as variáveis de ambiente com `python-dotenv`.

---

## Como Executar

```bash
python run.py
```

A aplicação será iniciada em:

```
http://127.0.0.1:5000
```

---

## Endpoint

### POST /api/youtube

### Body (JSON)

```json
{
  "channel_name": "Curso em Vídeo",
  "tags": ["python", "iniciante"]
}
```

### Resposta (JSON)

```json
{
  "channel_name": "Curso em Vídeo",
  "videos": [
    {
      "title": "Python para Iniciantes",
      "description": "...",
      "tags": ["python", "iniciante"],
      "publish_date": "2023-05-15T14:30:00Z",
      "views": 100000,
      "likes": 5000,
      "comment_count": 300,
      "duration": "PT15M30S"
    }
  ]
}
```

---

## Fluxo da Aplicação

1. Recebe o nome do canal e as tags.
2. Busca o `channel_id` na API do YouTube.
3. Obtém a playlist de uploads do canal.
4. Lista os vídeos da playlist.
5. Busca detalhes completos dos vídeos.
6. Filtra os vídeos com base nas tags.
7. Retorna o resultado em JSON.

---

## Tratamento de Erros

A API retorna mensagens de erro em formato JSON para:

* JSON ausente no body
* Entrada inválida
* Canal não encontrado
* Erros internos da aplicação
