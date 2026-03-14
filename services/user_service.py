# from database.db import mysql

# class UserService:

#     @staticmethod
#     def create_user(data):
#         cur = mysql.connection.cursor()

#         query = """
#         INSERT INTO users (name, email, age)
#         VALUES (%s,%s,%s)
#         """

#         cur.execute(query, (data["name"], data["email"], data["age"]))
#         mysql.connection.commit()

#         return {"message": "User created"}

#     @staticmethod
#     def get_users():
#         cur = mysql.connection.cursor()

#         cur.execute("SELECT * FROM users")

#         users = cur.fetchall()

#         return {"users": users}

#     @staticmethod
#     def get_user(id):
#         cur = mysql.connection.cursor()

#         cur.execute("SELECT * FROM users WHERE id=%s", (id,))

#         user = cur.fetchone()

#         return {"user": user}

#     @staticmethod
#     def update_user(id, data):
#         cur = mysql.connection.cursor()

#         query = """
#         UPDATE users
#         SET name=%s, email=%s, age=%s
#         WHERE id=%s
#         """

#         cur.execute(query, (data["name"], data["email"], data["age"], id))

#         mysql.connection.commit()

#         return {"message": "User updated"}

#     @staticmethod
#     def delete_user(id):
#         cur = mysql.connection.cursor()

#         cur.execute("DELETE FROM users WHERE id=%s", (id,))

#         mysql.connection.commit()

#         return {"message": "User deleted"}



from models.user_model import User
from database.db import db

class UserService:

    @staticmethod
    def create_user(data):
        user = User(
            name=data["name"],
            email=data["email"],
            age=data["age"]
        )

        db.session.add(user)
        db.session.commit()

        return user.to_dict()


    @staticmethod
    def get_users():
        users = User.query.all()
        return [user.to_dict() for user in users]


    @staticmethod
    def get_user(id):
        user = User.query.get(id)

        if not user:
            return {"error": "User not found"}

        return user.to_dict()


    @staticmethod
    def update_user(id, data):
        user = User.query.get(id)

        if not user:
            return {"error": "User not found"}

        user.name = data["name"]
        user.email = data["email"]
        user.age = data["age"]

        db.session.commit()

        return user.to_dict()


    @staticmethod
    def delete_user(id):
        user = User.query.get(id)

        if not user:
            return {"error": "User not found"}

        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted"}