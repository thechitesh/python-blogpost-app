from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#scret key is added to protect agains csrf other hacks
app.config['SECRET_KEY'] = '8feff63c1e248b6b1bd50e1efff2fca1'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


# this import is done here, as there is routes import app from __init__ and this will create cyclic dependency 
# and hence will fail. If we import routes before app iniitialization.
from flaskblog import routes