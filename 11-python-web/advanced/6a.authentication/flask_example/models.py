# Now, we added a 'password' field and removed the unused 'phone' field from the 'user' table.
# We also added a support for the login manager.

from datetime import datetime
from flask_example import db, login_manager  ### New
import flask_login 

@login_manager.user_loader   # Defines a function that loads the given user id from the DB.
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,flask_login.UserMixin):   # Double inheritance: db.Model, and flask_login.UserMixin
    id = db.Column(db.Integer , primary_key= True)
    username = db.Column(db.String(20) , unique=True, nullable = False)
    email = db.Column(db.String(20) , unique=True, nullable = False)
    password = db.Column(db.String(60), nullable=False)   ### New
    profile_img = db.Column(db.String(20), nullable= False , default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username!r} ,{self.email!r},{self.profile_img!r})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"