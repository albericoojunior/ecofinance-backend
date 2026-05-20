# EcoFinance Backend

API para gerenciamento de carteiras, metas financeiras e simulações de investimentos.

## Como rodar o projeto

### Usando Docker Compose

1. Configure o arquivo `.env` com as variáveis necessárias (veja `app/config.py`).
2. Execute:

```bash
docker-compose up --build
```

A API estará disponível em: http://localhost:8000

### Rodando localmente (sem Docker)

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure o arquivo `.env`.
3. Execute:

```bash
python run.py
```

---

## Rotas da API

### Auth

- `POST /auth/register` — Cadastro de usuário
  - **Body:** `{ nome, cpf, email, senha }`
  - **Permissão:** Público

- `POST /auth/login` — Login do usuário
  - **Body:** `{ email, senha }`
  - **Permissão:** Público
  - **Retorno:** `{ access_token, token_type }`

### Carteira

- `GET /carteira/` — Listar carteira do usuário
  - **Permissão:** (A ser implementado: requer autenticação)

### Metas

- `GET /metas/` — Listar metas financeiras
  - **Permissão:** (A ser implementado: requer autenticação)

### Simulações

- `POST /simulacoes/` — Simular investimento
  - **Body:** `{ tipo_calculo, valor, taxa, tempo }`
  - **Permissão:** (A ser implementado: requer autenticação)

---

## Permissões e Autenticação

- O registro e login são públicos.
- As demais rotas devem ser protegidas por autenticação JWT (a implementar).
- O token JWT é retornado no login e deve ser enviado no header `Authorization: Bearer <token>`.

---

## Tecnologias
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker

---

## Estrutura de Pastas

- `app/` — Código principal
  - `models/` — Modelos do banco
  - `routes/` — Rotas da API
  - `schemas/` — Schemas Pydantic
  - `services/` — Lógica de negócio

---

## Exemplo de arquivo `.env`

```
DATABASE_URL=postgresql://postgres:postgres@db:5432/ecofinance
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

- `DATABASE_URL`: URL de conexão com o banco de dados PostgreSQL.
- `SECRET_KEY`: Chave secreta para geração dos tokens JWT.
- `ALGORITHM`: Algoritmo usado para o JWT (ex: HS256).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tempo de expiração do token em minutos.
