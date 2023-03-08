from datetime import datetime
from flask_example import db

class User(db.Model):
    id = db.Column(db.Integer , primary_key= True)
    username = db.Column(db.String(20) , unique=True, nullable = False)
    email = db.Column(db.String(20) , unique=True, nullable = False)
    phone = db.Column(db.Integer , unique = True)
    profile_img = db.Column(db.String(20), nullable= False , default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.username!r} ,{self.email!r},{self.phone!r},{self.profile_img!r})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"