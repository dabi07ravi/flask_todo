# import os

# class Config:
#     MYSQL_HOST = "localhost"
#     MYSQL_USER = "root"
#     MYSQL_PASSWORD = "root@12345"
#     MYSQL_DB = "flask_users"


class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root%4012345@localhost/flask_users"
    SQLALCHEMY_TRACK_MODIFICATIONS = False