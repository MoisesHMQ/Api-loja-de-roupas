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

