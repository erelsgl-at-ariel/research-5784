# We put in 'models.py' the classes that represent objects in the database.

from datetime import datetime
from flask_example import db

# Define the "user" table: (note: table name is all lowercase)
class User(db.Model):
    # Define the columns in the user table:
    id = db.Column(db.Integer , primary_key= True)
    username = db.Column(db.String(20) , unique=True, nullable = False)
    email = db.Column(db.String(20) , unique=True, nullable = False)
    phone = db.Column(db.Integer , unique = True)
    profile_img = db.Column(db.String(20), nullable= False , default='default.jpg')

    # Define the relationship between the User and the Post table:
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.id!r}, {self.username!r}, {self.email!r}, {self.phone!r}, {self.profile_img!r})'


# Define the "post" table:
class Post(db.Model):
    # Define the columns in the post table:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    # Define the relationship between the User and the Post table:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # The "author" key in the Post table is related to the "id" key in the user table.

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

