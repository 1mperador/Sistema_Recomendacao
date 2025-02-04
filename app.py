from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recomendacoes"]
colecao = db["itens"]

# Rota inicial (listar itens)
@app.route("/")
def index():
    filme = colecao.find_one()  # Busca o primeiro filme do banco
    if not filme:  # Caso o banco esteja vazio
        filme = {
            "titulo": "Nenhum filme cadastrado",
            "descricao": "Adicione filmes para exibir aqui.",
            "estrelas": 0
        }
    return render_template("index.html", filme=filme)


# Rota para adicionar itens
@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        tags = request.form.get("tags").split(",")  # Separar tags por vírgula
        colecao.insert_one({"titulo": titulo, "descricao": descricao, "tags": tags})
        return redirect(url_for("index"))  # Corrigido para "index"
    return render_template("adicionar.html")


# Rota para buscar itens por tag
@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultados = []
    if request.method == "POST":
        tag = request.form.get("tag")
        resultados = colecao.find({"tags": tag})
    return render_template("buscar.html", resultados=resultados)

@app.route("/")
def home():
    filme = colecao.find_one()  # Busca o primeiro filme do banco
    if not filme:  # Caso o banco esteja vazio
        filme = {
            "titulo": "Nenhum filme cadastrado",
            "descricao": "Adicione filmes para exibir aqui.",
            "estrelas": 0
        }
    return render_template("index.html", filme=filme)

itens = [
    {"titulo": "Filme 1", "descricao": "Descrição do filme 1"},
    {"titulo": "Filme 2", "descricao": "Descrição do filme 2"}
]



if __name__ == "__main__":
    app.run(debug=True)
