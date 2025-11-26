from flask import Flask
from models.modelo import db
from controllers.views import init_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "static/img"

db.init_app(app)

with app.app_context():
    db.create_all()

init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)