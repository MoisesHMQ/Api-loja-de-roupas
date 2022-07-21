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