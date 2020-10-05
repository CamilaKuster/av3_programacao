#para executar usar o flask run
from flask import Flask, jsonify 
from flask_sqlalchemy import SQLAlchemy
import json 
import os
import datetime

#criando o app para armazenar td
app = Flask(__name__)
# se não colocar a sentença abaixo não localiza o app
FLASK_APP = app

# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'clientes.db')


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
# tres barras para indicar que é um arquivo local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)
#sempre adicionar tudo na aplicação