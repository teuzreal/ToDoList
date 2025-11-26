from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    concluida = db.Column(db.Boolean, default=False)
    data = db.Column(db.Date, nullable=True)
    imagem = db.Column(db.String(200), nullable=True)