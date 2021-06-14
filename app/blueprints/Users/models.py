from app import db, login 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from time import time
from flask import current_app as app
import base64
from datetime import datetime, timedelta
import os

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    displayname = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    verified = db.Column(db.Boolean, unique=False, default=True)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.column(db.DateTime)
    
    def __init__(self, username, displayname, password, email):
        self.username = username
        self.diaplayname = displayname
        self.password = generate_password_hash(password)
        self.email = email
        self.verified = True
        
    def __repr__(self):
        return f'<User | {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'displayname': self.displayname,
            'email': self.email,
            'avatar': self.avatar,
            'verified': self.verified,
        }

    def from_dict(self,data):
        for field in ['displayname', 'email']:
            if field in data:
                setattr(self, field, data[field])
                
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token
    
    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=t)
        
    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user