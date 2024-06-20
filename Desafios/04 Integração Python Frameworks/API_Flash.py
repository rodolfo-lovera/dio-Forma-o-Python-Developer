"""
Realizado a instalação das bibliotecas flask e flask_ngrok
- pip install flask
- pip install flask_ngrok
"""

import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import(
    request, jsonify, Flask
)
import random as rk

app = Flask(__name__)
run_with_ngrok(app)

json = [{
            "nome": "Miltom Hatoum",
            "cpf": "123456",
            "idade": 50,
            "cidade": "Rio de Janeiro",
            "estado": "RJ"
        }, {
            "nome": "Clarice Lispector",
            "cpf": "564231",
            "idade": 30,
            "cidade": "Belém",
            "estado": "PA",
        }, {
            "nome": "Jorge Amado",
            "cpf": "654321",
            "idade": 61,
            "cidade": "Salvador",
            "estado": "BA",
        }, {
            "nome": "Aline Bei",
            "cpf": "456342",
            "idade": 28,
            "cidade": "São Paulo",
            "estado": "SP",
        }  ]

@app.route("/")

def index():
    return " TO CHECK IN PUT ADD '/input' TO THE URL AND CHECK OUT PUT ADD '/output' TO THE URL."

@app.route("/input")

def input_json():
    return jsonify(json)

@app.route('/output', method=['GET','POST'])

def pred_json():
    pred = rk.choice(["positive","negative"])
    nd = json
    nd["prediction"]=pred
    return jsonify(nd)

app.run()