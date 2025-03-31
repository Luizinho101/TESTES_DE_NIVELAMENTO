# Flask API para Busca de Operadoras

Este projeto é uma API desenvolvida com Flask para buscar operadoras registradas no banco de dados PostgreSQL.

## 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- Flask-CORS
- PostgreSQL
- Psycopg2

## 📂 Estrutura do Projeto

```bash
📦 projeto
├── app.py          
├── config.py       
├── database.py    
├── routes.py      
├── requirements.txt
└── README.md       
```

## ⚙️ Configuração do Banco de Dados

Antes de rodar o projeto, configure o banco de dados no arquivo `config.py`:

```python
DATABASE_CONFIG = {
    "host": "localhost",
    "database": "TesteTecnico",
    "user": "postgres",
    "password": "sua_senha"
}
```

## ▶️ Como Rodar o Projeto

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/projeto-flask.git
   cd projeto-flask
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   venv\Scripts\activate     
   ```
3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute o servidor**
   ```bash
   python app.py
   ```
5. **Acesse a API**
   - Endpoint de busca: `http://127.0.0.1:5000/search?q=nome`

## 📌 Exemplo de Uso

### Requisição:
```bash
curl "http://127.0.0.1:5000/search?q=operadora"
```

### Resposta:
```json
[
    {
        "id": 1,
        "razao_social": "Operadora Exemplo S/A",
        "nome_fantasia": "Operadora Exemplo"
    }
]
```

## 📜 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo! 🚀

