from datetime import datetime, timezone, timedelta
from typing import Optional
from flask import Blueprint, request, jsonify
from config import db

# Definir um blueprint para as rotas principais
user = Blueprint("user", __name__, url_prefix="/user")

from models.models import User

@user.route("/", methods=["GET"])
def list_users():
    users = User.query.all()  # Pega todos os usuários
    return jsonify(
        [
            {
                "id": u.id,
                "name": u.name,
                "cpf": u.cpf,
                "date": u.date.strftime("%Y-%m-%d"),
            }
            for u in users
        ]
    )


@user.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    existing_user = User.query.filter_by(cpf=data["cpf"]).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    user = User(
        name=data["name"],
        cpf=data["cpf"],
        date=datetime.strptime(data["date"], "%d-%m-%Y").date(),
    )

    db.session.add(user)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Usuário criado com sucesso",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "cpf": user.cpf,
                    "date": user.date,
                },
            }
        ),
        201,
    )


@user.route("/<int:user_id>", methods=["PATCH"])
def edit_user(user_id):
    data = request.get_json()

    user: Optional[User] = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 400

    user.cpf = data["cpf"]
    user.name = data["name"]
    user.date = datetime.strptime(data["date"], "%d-%m-%Y").date()

    db.session.add(user)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Usuário editado com sucesso",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "cpf": user.cpf,
                    "date": user.date,
                },
            }
        ),
        200,
    )


@user.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user: Optional[User] = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 400

    user_name = user.name
    User.query.filter_by(id=user_id).delete()

    db.session.commit()

    return jsonify({"message": f"Usuário {user_name} removido com sucesso"}), 200
