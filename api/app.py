from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

from flask import Flask, jsonify, request


# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do MongoDB
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client["recomendacao"]
collection = db["filmes"]

# Inicializando o Flask
app = Flask(__name__)

# Rota inicial
@app.route("/")
def home():
    return jsonify({"message": "Bem-vindo ao sistema de recomendações de filmes!"})

# Rota para buscar todos os filmes
@app.route("/filmes", methods=["GET"])
def listar_filmes():
    filmes = list(collection.find({}, {"_id": 0}))  # Não incluir o _id na resposta
    return jsonify(filmes)

# Rota para adicionar um novo filme
@app.route("/filmes", methods=["POST"])
def adicionar_filme():
    novo_filme = request.json
    if not novo_filme.get("nome") or not novo_filme.get("descricao"):
        return jsonify({"error": "Os campos 'nome' e 'descricao' são obrigatórios."}), 400
    collection.insert_one(novo_filme)
    return jsonify({"message": "Filme adicionado com sucesso!"}), 201

# Rota para buscar um filme pelo nome
@app.route("/filmes/<nome>", methods=["GET"])
def buscar_filme(nome):
    filme = collection.find_one({"nome": nome}, {"_id": 0})  # Não incluir o _id na resposta
    if filme:
        return jsonify(filme)
    return jsonify({"error": "Filme não encontrado."}), 404

# Rota para atualizar um filme
@app.route("/filmes/<nome>", methods=["PUT"])
def atualizar_filme(nome):
    dados_atualizados = request.json
    resultado = collection.update_one({"nome": nome}, {"$set": dados_atualizados})
    if resultado.matched_count > 0:
        return jsonify({"message": "Filme atualizado com sucesso!"})
    return jsonify({"error": "Filme não encontrado."}), 404

# Rota para deletar um filme
@app.route("/filmes/<nome>", methods=["DELETE"])
def deletar_filme(nome):
    resultado = collection.delete_one({"nome": nome})
    if resultado.deleted_count > 0:
        return jsonify({"message": "Filme deletado com sucesso!"})
    return jsonify({"error": "Filme não encontrado."}), 404

# Rodando a aplicação
if __name__ == "__main__":
    app.run(debug=True)
