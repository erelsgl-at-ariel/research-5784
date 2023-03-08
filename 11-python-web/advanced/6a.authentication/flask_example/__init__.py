# Now, we add bcrypt and login support.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # New
from flask_login import LoginManager # New

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecf6e975838a2f7bf3c5dbe7d55ebe5b'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # New
login_manager = LoginManager(app)  # New
login_manager.login_view = 'login'   # Tell the login manager where the login page is located.
login_manager.login_message_category = 'info'   # Category of message for non-logged-in user trying to access a login-only page.

from flask_example import routes



