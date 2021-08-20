from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from main.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # now we have SQLite database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'  # setting color to error msg of account

mail = Mail(app)


# import instance of blueprint class

from main.users.routes import users
from main.posts.routes import posts
from main.general.routes import general

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(general)