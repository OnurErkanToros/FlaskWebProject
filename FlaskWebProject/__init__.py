
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'yourkey'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'yourkey'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'yourmail'
app.config['MAIL_PASSWORD'] = 'yourmailpassword'


db = SQLAlchemy(app)
loginManager = LoginManager(app)
mail = Mail(app)
from atmacaFlask import routes