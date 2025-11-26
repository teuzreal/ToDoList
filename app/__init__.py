from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

caminho_banco = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'tarefa.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_banco}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'chave-secreta'

db = SQLAlchemy(app)

from app.controllers import views

with app.app_context():
    db.create_all()