from datetime import datetime, timezone, timedelta
from flask import Blueprint, request, jsonify
from app import db

import jwt
import time
import os
import dotenv

dotenv.load_dotenv()
secret = os.getenv('JWT_SECRET')
algorithm = os.getenv('ALGORYTHM')


# Definir um blueprint para as rotas principais
auth = Blueprint("auth", __name__, url_prefix="/auth")

from models.models import User


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    existing_user = User.query.filter_by(cpf=data["cpf"]).first()
    if not existing_user:
        return jsonify({"error": "User don't exist"}), 400

    token_payload = {
        'cpf': data["cpf"],
        'data_nasc': data["data_nasc"]
    }

    token = jwt.encode(token_payload, secret, algorithm)
    print(token)
    print(jwt.decode(token, secret, algorithm))

    return 200
