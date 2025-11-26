from flask import render_template, request, redirect, url_for, current_app
from models.modelo import db, Tarefa
from datetime import datetime
import os

def init_routes(app):
    @app.route("/")
    def index():
        busca = request.args.get("busca")
        filtro = request.args.get("filtro")

        query = Tarefa.query

        if busca:
            query = query.filter(Tarefa.titulo.contains(busca))

        if filtro == "concluidas":
            query = query.filter_by(concluida=True)
        elif filtro == "pendentes":
            query = query.filter_by(concluida=False)

        tarefas = query.order_by(Tarefa.data.desc()).all()

        return render_template("index.html", tarefas=tarefas)


    @app.route("/adicionar", methods=["GET", "POST"])
    def adicionar():
        if request.method == "POST":
            titulo = request.form["titulo"]
            descricao = request.form["descricao"]
            data = request.form["data"]

            imagem = None
            file = request.files.get("imagem")
            if file and file.filename:
                caminho = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
                file.save(caminho)
                imagem = file.filename

            nova = Tarefa(
                titulo=titulo,
                descricao=descricao,
                data=datetime.strptime(data, "%Y-%m-%d") if data else None,
                imagem=imagem
            )

            db.session.add(nova)
            db.session.commit()

            return redirect(url_for("index"))

        return render_template("adicionar.html")


    @app.route("/editar/<int:id>", methods=["GET", "POST"])
    def editar(id):
        tarefa = Tarefa.query.get(id)

        if request.method == "POST":
            tarefa.titulo = request.form["titulo"]
            tarefa.descricao = request.form["descricao"]
            tarefa.data = datetime.strptime(request.form["data"], "%Y-%m-%d") if request.form["data"] else None
            tarefa.concluida = "concluida" in request.form

            file = request.files.get("imagem")
            if file and file.filename:
                caminho = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
                file.save(caminho)
                tarefa.imagem = file.filename

            db.session.commit()
            return redirect(url_for("index"))

        return render_template("editar.html", tarefa=tarefa)


    @app.route("/remover/<int:id>")
    def remover(id):
        tarefa = Tarefa.query.get(id)
        db.session.delete(tarefa)
        db.session.commit()
        return redirect(url_for("index"))
    
    @app.route("/concluir/<int:id>")
    def concluir(id):
        tarefa = Tarefa.query.get(id)
        tarefa.concluida = True
        db.session.commit()
        return redirect(url_for("index"))
