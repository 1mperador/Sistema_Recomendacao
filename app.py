from flask import Flask, render_template, request, redirect, url_for
import pymongo
import json

app = Flask(__name__)

# Carregar dados do MongoDB ou do JSON

def carregar_dados():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["recomendacoes"]
        collection = db["itens"]
        return list(collection.find({}, {"_id": 0}))
    except:
        with open("filmes.json", "r", encoding="utf-8") as f:
            return json.load(f)

# Dados carregados
filmes = carregar_dados()

@app.route("/")
def index():
    filme = filmes[0] if filmes else {
        "titulo": "Nenhum filme cadastrado",
        "descricao": "Adicione filmes para exibir aqui.",
        "estrelas": 0
    }
    return render_template("index.html", filme=filme)

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        tags = request.form.get("tags").split(",")  # Separar tags por vírgula
        
        novo_filme = {"titulo": titulo, "descricao": descricao, "tags": tags}
        
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["recomendacoes"]
            collection = db["itens"]
            collection.insert_one(novo_filme)
        except:
            filmes.append(novo_filme)
            with open("filmes.json", "w", encoding="utf-8") as f:
                json.dump(filmes, f, indent=4, ensure_ascii=False)
        
        return redirect(url_for("index"))
    return render_template("adicionar.html")

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultados = []
    if request.method == "POST":
        tag = request.form.get("tag")
        resultados = [filme for filme in filmes if tag in filme.get("tags", [])]
    return render_template("buscar.html", resultados=resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
