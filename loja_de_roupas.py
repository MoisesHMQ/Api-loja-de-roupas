from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)


cliente = []

@app.route("/cadastrar/clientes", methods=['POST'])
def cadastrar():
    registro = request.json 
    for user in cliente:
        if user["email"] == registro["email"]:  
            return {"Algo deu errado.":"Esse email ja existe."}
    registro = {
        "identificação": str(uuid.uuid4()),
        "email": registro["email"],
        "senha": registro["senha"]
        }
    cliente.append(registro)
    return jsonify(registro)

@app.route("/login", methods=['POST'])
def logar():
    login = request.json
    for login in cliente:
        if login["email"] == login["email"] and login["senha"] == login["senha"]:
            return{"Status":"Logado."}
        else:
            return{"Status":"Usuario ou Senha Incorretos."}

@app.route("/banco_de_usuarios")
def usuarios():
    return jsonify(cliente)

@app.route("/excluir/usuarios", methods=['POST'])
def excluir_usuarios():
    user_excluir = request.json
    print(cliente)
    for list in cliente:
        if list["identificação"] == user_excluir["identificação"]:
            cliente.remove(list)
            return user_excluir

camisa  = []
bermuda = []
chinelo = []

@app.route("/camisas", methods=['POST'])
def camisetas():
    tipo = request.json
    for tipo_camisas in camisa:
        if tipo_camisas["camisa"] == tipo["camisa"]:
            return {"status": "Produto já cadastrado."}
    tipo = {
        "codigo_barras": str(uuid.uuid4()),
        "tamanho":tipo["tamanho"],
        "camisa": tipo["camisa"],
        "cor":tipo["cor"]
    }
    camisa.append(tipo)
    return jsonify(tipo)

@app.route("/bermuda", methods=['POST'])
def bermudas():
    modelo = request.json
    for modelo_gesso in bermuda:
        if modelo_gesso["bermuda"] == modelo["bermuda"]:
            return {"status": "Produto já cadastrado."}
    modelo = {
        "codigo_barras": str(uuid.uuid4()),
        "bermuda": modelo["bermuda"],
        "tamanho":modelo["tamanho"]
        }
    bermuda.append(modelo)
    return jsonify(modelo)

@app.route("/chinelo", methods=['POST'])
def chinelos():
    modelo = request.json
    for modelo_gesso in chinelo:
        if modelo_gesso["chinelo"] == modelo["chinelo"]:
            return {"status": "Produto já cadastrado."}
    modelo = {
        "codigo_barras": str(uuid.uuid4()),
        "chinelo": modelo["chinelo"],
        "tamanho":modelo["tamanho"]
        }
    chinelo.append(modelo)
    return jsonify(modelo)

@app.route("/carrinho/compras")
def carrinho():
    return jsonify(camisa,bermuda,chinelo)


@app.route("/excluir/camisa", methods=['POST'])
def excluir_camisas():
    itens = request.json
    print(camisa)
    for dell in camisa:
        if dell["codigo_barras"] == itens["codigo_barras"]:
            camisa.remove(dell)
            return itens

@app.route("/excluir/bermudas", methods=['POST'])
def excluir_bermudas():
    berma = request.json
    print(bermuda)
    for dell in bermuda:
        if dell["codigo_barras"] == berma["codigo_barras"]:
            bermuda.remove(dell)
            return berma

@app.route("/excluir/chinelo", methods=['POST'])
def excluir_chinelo():
    sandalia = request.json
    print(chinelo)
    for dell in chinelo:
        if dell["codigo_barras"] == sandalia["codigo_barras"]:
            chinelo.remove(dell)
            return sandalia


app.run()

