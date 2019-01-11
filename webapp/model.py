from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50),index=True,unique=True)
    password=db.Column(db.String(128))
    email=db.Column(db.String(128),unique=True)
    dateRegistration=(db.String(10))
    userTelegrammChat=db.Column(db.String(128),unique=True)

    def set_password(self, password):
        self.password=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)