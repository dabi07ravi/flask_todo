from models.user_model import User
from database.db import db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()

class AuthService:

    @staticmethod
    def register(data):

        hashed_password = bcrypt.generate_password_hash(
            data["password"]
        ).decode("utf-8")

        user = User(
            name=data["name"],
            email=data["email"],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User registered"}


    @staticmethod
    def login(data):

        user = User.query.filter_by(email=data["email"]).first()

        if not user:
            return {"error": "Invalid credentials"}

        if not bcrypt.check_password_hash(
            user.password,
            data["password"]
        ):
            return {"error": "Invalid credentials"}

        token = create_access_token(identity=str(user.id))

        return {"token": token}