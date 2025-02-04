from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do MongoDB
MONGO_URI = os.getenv("MONGO_URI")  # Certifique-se de que esta variável está no .env

client = MongoClient(MONGO_URI, server_api=ServerApi('1'), maxPoolSize=10)

# Verificar se a URI do MongoDB foi carregada corretamente
if not MONGO_URI:
    raise ValueError("Erro: A variável de ambiente MONGO_URI não foi encontrada. Verifique seu arquivo .env.")

# Configurar conexão com MongoDB
try:
    client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
    db = client["recomendacao"]
    collection = db["filmes"]
except Exception as e:
    raise ConnectionError(f"Erro ao conectar ao MongoDB: {e}")

# Inicializando o Flask
app = Flask(__name__)

# Rota inicial
@app.route("/")
def hello():
    return jsonify({"message": "Bem-vindo ao sistema de recomendações de filmes!"})

print("MongoDB URI:", MONGO_URI)

# reduzao de dados para teste
@app.route("/filmes", methods=["GET"])
def listar_filmes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    filmes = list(collection.find({}, {"_id": 0}).skip((page - 1) * limit).limit(limit))
    return jsonify(filmes)


# Rota para adicionar um novo filme
@app.route("/filmes", methods=["POST"])
def adicionar_filme():
    novo_filme = request.json
    if not novo_filme.get("nome") or not novo_filme.get("descricao"):
        return jsonify({"error": "Os campos 'nome' e 'descricao' são obrigatórios."}), 400
    try:
        collection.insert_one(novo_filme)
        return jsonify({"message": "Filme adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar filme: {e}"}), 500

# Rota para buscar um filme pelo nome
@app.route("/filmes/<nome>", methods=["GET"])
def buscar_filme(nome):
    try:
        filme = collection.find_one({"nome": nome}, {"_id": 0})  # Não incluir o _id na resposta
        if filme:
            return jsonify(filme), 200
        return jsonify({"error": "Filme não encontrado."}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar filme: {e}"}), 500

# Rota para atualizar um filme
@app.route("/filmes/<nome>", methods=["PUT"])
def atualizar_filme(nome):
    dados_atualizados = request.json
    try:
        resultado = collection.update_one({"nome": nome}, {"$set": dados_atualizados})
        if resultado.matched_count > 0:
            return jsonify({"message": "Filme atualizado com sucesso!"}), 200
        return jsonify({"error": "Filme não encontrado."}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao atualizar filme: {e}"}), 500

# Rota para deletar um filme
@app.route("/filmes/<nome>", methods=["DELETE"])
def deletar_filme(nome):
    try:
        resultado = collection.delete_one({"nome": nome})
        if resultado.deleted_count > 0:
            return jsonify({"message": "Filme deletado com sucesso!"}), 200
        return jsonify({"error": "Filme não encontrado."}), 404
    except Exception as e:
        return jsonify({"error": f"Erro ao deletar filme: {e}"}), 500

# Rodando a aplicação
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
