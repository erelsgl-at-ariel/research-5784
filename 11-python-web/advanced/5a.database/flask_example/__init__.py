# The '__init__.py' collects the main project definitions in one place.
# app - the web application to run.
# db  - the database.

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'  # Connect to an SQLite database in file 'site.db' in the current folder.
db = SQLAlchemy(app)
from flask_example import routes
