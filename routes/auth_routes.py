from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    result = AuthService.register(data)
    return jsonify(result)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    result = AuthService.login(data)
    return jsonify(result)


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = get_jwt_identity()
    print("userrrrrid", user_id)

    return jsonify({
        "message": "Access granted",
        "user_id": user_id
    })