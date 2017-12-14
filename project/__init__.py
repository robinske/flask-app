from flask import Flask, render_template

app = Flask(__name__)

# Setup the app with the config.py file
app.config.from_object('config')

# Setup the database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Setup the mail server
from flask_mail import Mail
mail = Mail(app)

# Setup the password crypting
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Import the views
from project.views import main, user, error
app.register_blueprint(user.userbp)

# Setup the user login process
from flask_login import LoginManager
from project.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'userbp.signin'

@login_manager.user_loader
def load_user(email):
    return User.query.filter(User.email == email).first()
