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

## Serviços Azure utilizados

| Serviço | Justificativa |
|---|---|
| **Azure App Service** | PaaS gerenciado — sem precisar configurar SO, patches ou SSH. Deploy simples com `az webapp up`. |
| **Azure Database for PostgreSQL Flexible Server** | Banco relacional gerenciado, backups automáticos, alta disponibilidade, sem gerenciar servidor de banco. |

## Estrutura do Projeto

```
cloud-final/
├── app/
│   ├── main.py          # FastAPI app + lifespan
│   ├── database.py      # Conexão SQLAlchemy
│   ├── models.py        # Modelo Task
│   ├── schemas.py       # Schemas Pydantic
│   ├── routers/
│   │   └── tasks.py     # Rotas CRUD
│   └── templates/
│       └── index.html   # Interface web
├── requirements.txt
├── .env.example
├── startup.sh
└── README.md
```

## Como rodar localmente

### Pré-requisitos
- Python 3.11+
- PostgreSQL rodando localmente (ou Docker)

### Passos

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd ToDo-App

# 2. Crie o ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o banco de dados
cp .env.example .env
# Edite .env com suas credenciais PostgreSQL

# 5. Execute a aplicação
uvicorn app.main:app --reload
```

Acesse: http://localhost:8000

## Deploy no Azure

### Pré-requisitos
- [Azure CLI](https://learn.microsoft.com/pt-br/cli/azure/install-azure-cli) instalado
- Conta Azure com créditos de estudante

### Passo a passo

**1. Login no Azure**
```bash
az login
```

**2. Criar Resource Group**
```bash
az group create --name rg-cloud-final --location brazilsouth
```

**3. Criar banco de dados PostgreSQL**

No Portal Azure:
- Pesquise por "Azure Database for PostgreSQL"
- Selecione "Flexible Server"
- Resource Group: `rg-cloud-final`
- Nome do servidor: `pg-cloud-final`
- Tier: Burstable, B1ms
- Crie um banco chamado `tododb`
- Habilite "Allow public access from any Azure service"

**4. Criar App Service e fazer deploy**
```bash
az webapp up \
  --name todo-app-cloud-final \
  --resource-group rg-cloud-final \
  --runtime PYTHON:3.11 \
  --sku F1
```

**5. Configurar variável de ambiente**

No Portal Azure → App Service → Configuração → Configurações do aplicativo:
- Adicione `DATABASE_URL` com a connection string do PostgreSQL

Formato:
```
postgresql://admin_user:senha@pg-cloud-final.postgres.database.azure.com/tododb?sslmode=require
```

**6. Configurar startup command**

No Portal Azure → App Service → Configuração → Configurações gerais:
- Startup command: `bash startup.sh`

**7. Reiniciar o App Service**
```bash
az webapp restart --name todo-app-cloud-final --resource-group rg-cloud-final
```

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
