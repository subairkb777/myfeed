from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail  import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '32552fea32f5ccc3f681b4442e6f87e9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lolanfan.777@gmail.com'
app.config['MAIL_PASSWORD'] = 'winter123!'
mail = Mail(app)


from flaskblog import routes