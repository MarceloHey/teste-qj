from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# Configuração do banco de dados (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar o SQLAlchemy com a aplicação Flask
db = SQLAlchemy(app=app)

from routes import user_routes, auth_routes

app.register_blueprint(user_routes.user)
app.register_blueprint(auth_routes.auth)





