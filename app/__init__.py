from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plus9jatv.sqlite'
app.config['SECRET_KEY'] ='rgserjgjrhrehj[rhjshj[sh[hjs[t'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(app)



from app.auth import auth as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app.models import Role, User
Role.insert_roles()
Role.query.all()

from app import routes
