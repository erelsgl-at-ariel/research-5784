from flask import Flask, render_template
app = Flask(__name__)

import dotenv, os
dotenv.load_dotenv()  # load FLASK_RUN_PORT

users = [   # Simulates reading from database.
    {'name': 'Joee Javany',
    'email': 'joo@example.com',
    'phone': '111-1111'},
    {'name': 'Tom Pythonovitch',
    'email': 'python_is_coool@example.com',
    'phone': '222-2222'},
    {'name': 'Tami CPP',
    'email': 'cpp-forever@example.com',
    'phone': '222-2222'},
    {'name': 'Rusty Rust',
    'email': 'rust@example.com',
    'phone': '5555555'},
]

@app.route('/')
def hello_world():
    return render_template('homedynamic.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("FLASK_RUN_PORT"))
