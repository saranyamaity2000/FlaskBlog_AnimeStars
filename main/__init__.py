from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# as this app is being imported to many places so we have to be careful
# about circular imports , so anything we want to access should be imported down below everything

app.config['SECRET_KEY'] = '54869a0a55f9b9b8dbd8915596bbf36b'
'''
   the secret key is generated by 
   >>> import secrets 
   >>> secrets.token_hex(16)
   // now a 16 byte code will be generated randomly  
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # 3 forward slash '/' to specify relative path
db = SQLAlchemy(app)  # now we have SQLite database instance

# creating crypt  class for pass hash
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'  # setting color to error msg of account

from main import routes  # now the whole route.py will be executed