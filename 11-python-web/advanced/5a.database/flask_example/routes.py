# We put in 'routes.py' all code related to routing clients to pages. 

from flask import render_template
from flask_example import app

users = [
    {'name': 'Joee Javany',
    'email': 'joo@example.com',
    'phone': '111-1111'},
    {'name': 'Tom Pythonovitch',
    'email': 'python_is_coool@example.com',
    'phone': '222-2222'},
]
@app.route('/')
def hello_world():
    return render_template('home.html' , users = users)
