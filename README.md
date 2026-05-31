# Todo App — Projeto Final Cloud

Aplicação web de lista de tarefas (Todo App) desenvolvida com **Python + FastAPI**, hospedada no **Azure App Service** e com banco de dados **Azure Database for PostgreSQL**.

## Arquitetura

```
Usuário (Browser)
       │
       ▼
Azure App Service
  Python 3.11 / FastAPI / Uvicorn
       │
       ▼
Azure Database for PostgreSQL
  Flexible Server — tabela: tasks
```

Todos os recursos estão dentro do Resource Group `rg-cloud-final` na região **Brazil South**.

## Funcionalidades

- Adicionar tarefas
- Marcar tarefas como concluídas / desfazer
- Deletar tarefas
- Contador de tarefas concluídas

## Tecnologias

- **FastAPI** — framework web moderno para Python
- **SQLAlchemy** — ORM para comunicação com o banco
- **Jinja2** — templates HTML server-side
- **PostgreSQL** — banco de dados relacional
- **Azure App Service** — hospedagem da aplicação
- **Azure Database for PostgreSQL** — banco gerenciado na nuvem
