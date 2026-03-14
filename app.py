# from flask import Flask
# from config import Config
# from database.db import mysql
# from routes.user_routes import user_bp


# app = Flask(__name__)

# app.config.from_object(Config)
# mysql.init_app(app)

# app.register_blueprint(user_bp, url_prefix="/users")



# if __name__ == "__main__":
#     app.run(debug=True, port=3000)

from dotenv import load_dotenv
import os

load_dotenv()


from flask import Flask
from config import Config
from database.db import db
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager



app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

jwt = JWTManager(app)


app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(auth_bp, url_prefix="/auth")


migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT"))