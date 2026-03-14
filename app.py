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




from flask import Flask
from config import Config
from database.db import db
from routes.user_routes import user_bp
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(user_bp, url_prefix="/users")

migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True, port=3000)