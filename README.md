# CRUD em MongoDB com Python (pymongo)

Este projeto implementa as operações **CRUD** (Create, Read, Update, Delete) em um banco de dados **MongoDB**, utilizando a biblioteca `pymongo`.

---

## 📌 Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community) (local, Docker ou Atlas na nuvem)

### Instalando dependências

No terminal, dentro da pasta do projeto, rode:
```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` já inclui a biblioteca `pymongo`.

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/crud-mongodb.git
cd crud-mongodb
```

### 2. Verifique se o MongoDB está rodando
Se estiver rodando **localmente**, inicie o serviço MongoDB:
```bash
mongod
```

Se estiver rodando via **Docker**, use o comando:
```bash
docker run -d -p 27017:27017 --name mongodb mongo
```

Isso vai iniciar um container com o MongoDB na porta `27017`.

### 3. Execute o script principal
```bash
python main.py
```

---

## 📝 Estrutura do Projeto

```
crud-mongodb/
│-- main.py           # Arquivo principal com as operações CRUD
│-- requirements.txt  # Dependências do projeto
│-- README.md         # Documentação do projeto
```

---

## ⚡ Operações CRUD implementadas

- **Create** → Inserção de documentos na coleção `usuarios`
- **Read** → Listagem de todos os documentos cadastrados
- **Update** → Atualização de um usuário pelo nome
- **Delete** → Remoção de um usuário pelo nome

Exemplo de fluxo ao rodar `main.py`:

```
Usuários cadastrados com sucesso!
Lista de usuários:
{'_id': ObjectId('...'), 'nome': 'Alice', 'email': 'alice@email.com'}
{'_id': ObjectId('...'), 'nome': 'Bob', 'email': 'bob@email.com'}

Usuário atualizado!
Usuário removido!
```

---

## 🐳 Acessando o banco dentro do Docker

Se você criou o MongoDB com Docker, pode entrar no container com:
```bash
docker exec -it mongodb mongosh
```

E dentro do **Mongo Shell** rodar:
```js
show dbs
use meu_banco
show collections
db.usuarios.find().pretty()
```

Isso vai mostrar todos os usuários cadastrados no banco.

---

## 📚 O que foi feito neste projeto

1. Criado o arquivo `main.py` com as funções para **inserir, listar, atualizar e deletar** usuários.
2. Usada a biblioteca `pymongo` para conectar ao banco.
3. Criado um banco chamado **meu_banco** e a coleção **usuarios**.
4. Testado localmente e com Docker para garantir o funcionamento.
5. Documentado os passos neste `README.md` para facilitar a execução de quem nunca usou MongoDB.


