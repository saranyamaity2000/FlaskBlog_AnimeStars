from datetime import datetime
from main import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)
    # P is capital in Post as here we are referencing the 'Post' class
    # its a relationship to Post model
    # backref is similar to adding another column to post model with relationship
    # lazy = True means SQLAlchemy will load the data from database in one go considering necessary

    def __repr__(self):  # its a magic method
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #                               here we have used lower case u and i in 'user.id' because
    # here we are referencing user table.column in database , and in database everything is
    # stored in lowercase

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"
