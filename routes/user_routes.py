from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint("users", __name__)

@user_bp.route("/create", methods=["POST"])
def create_user():
    data = request.json
    result = UserService.create_user(data)
    return jsonify(result)

@user_bp.route("/", methods=["GET"])
def get_users():
    result = UserService.get_users()
    return jsonify(result)

@user_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    result = UserService.get_user(id)
    return jsonify(result)

@user_bp.route("/update/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    result = UserService.update_user(id, data)
    return jsonify(result)

@user_bp.route("/del/<int:id>", methods=["DELETE"])
def delete_user(id):
    result = UserService.delete_user(id)
    return jsonify(result)