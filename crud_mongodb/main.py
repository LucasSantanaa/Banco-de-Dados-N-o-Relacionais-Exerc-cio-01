from pymongo import MongoClient

# =============================
# CONFIGURAÇÃO DO MONGODB
# =============================

# Para conectar no MongoDB local
# client = MongoClient("mongodb://localhost:27017/")

# Para conectar no Docker (se rodando com --network bridge, localhost funciona)
client = MongoClient("mongodb://localhost:27017/")

# Para conectar no Atlas (troque pela sua connection string)
# client = MongoClient("mongodb+srv://usuario:senha@cluster0.mongodb.net/")

# Definindo o banco e a coleção
db = client["meu_banco"]
colecao = db["usuarios"]

# =============================
# FUNÇÕES CRUD
# =============================

def create_usuario(nome, email):
    """Cria um novo usuário no MongoDB"""
    usuario = {"nome": nome, "email": email}
    resultado = colecao.insert_one(usuario)
    print(f"✅ Usuário criado com ID: {resultado.inserted_id}")


def read_usuarios():
    """Lista todos os usuários cadastrados"""
    usuarios = colecao.find()
    print("\n📋 Usuários cadastrados:")
    for u in usuarios:
        print(u)


def update_usuario(nome_antigo, novo_nome):
    """Atualiza o nome de um usuário"""
    resultado = colecao.update_one(
        {"nome": nome_antigo},
        {"$set": {"nome": novo_nome}}
    )
    if resultado.modified_count > 0:
        print(f"🔄 Usuário '{nome_antigo}' atualizado para '{novo_nome}'.")
    else:
        print("⚠️ Nenhum usuário encontrado para atualizar.")


def delete_usuario(nome):
    """Deleta um usuário pelo nome"""
    resultado = colecao.delete_one({"nome": nome})
    if resultado.deleted_count > 0:
        print(f"🗑️ Usuário '{nome}' deletado com sucesso.")
    else:
        print("⚠️ Nenhum usuário encontrado para deletar.")


# =============================
# EXECUÇÃO DE TESTE
# =============================

if __name__ == "__main__":
    # Limpa a coleção para facilitar testes
    colecao.delete_many({})

    # CREATE
    create_usuario("Alice", "alice@email.com")
    create_usuario("Bob", "bob@email.com")

    # READ
    read_usuarios()

    # UPDATE
    update_usuario("Alice", "Alicia")

    # READ novamente
    read_usuarios()

    # DELETE
    delete_usuario("Bob")

    # READ final
    read_usuarios()
