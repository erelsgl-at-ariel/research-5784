from flask import Flask, render_template
app = Flask(__name__)

import dotenv, os
dotenv.load_dotenv()  # load FLASK_RUN_PORT

users = [
    {'name': 'Joee Javany',
    'email': 'joo@example.com',
    'phone': '111-1111'},
    {'name': 'Tom Pythonovitch',
    'email': 'python_is_coool@example.com',
    'phone': '222-2222'},
    {'name': 'abc',
    'email': 'xyz',
    'phone': '123'},
]

@app.route('/')
def hello_world():
    return render_template('layoutdynamic.html' , users = users, head = "Moriya")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("FLASK_RUN_PORT"))


