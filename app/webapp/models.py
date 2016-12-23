from flask_sqlalchemy import SQLAlchemy
from extensions import bcrypt
from flask_login import AnonymousUserMixin

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    subjects = db.relationship('Subject', backref='subject', lazy='dynamic')

    def __init__(self, username, password=None):
        self.username = username
        if password:
            self.set_password(password)
        
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return "<User: '{}'>".format(self.username)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cards = db.relationship('Card', backref='card', lazy='dynamic')

    def __init__(self, name, user_id, description=None):
        self.name = name
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return "<Subject: '{}'>".format(self.name)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(650))
    image_path = db.Column(db.String(100))
    correct_responses = db.Column(db.Integer)
    total_views = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    
    def __init__(self, name, description, subject_id, image_path=None):
        self.name = name
        self.description = description
        self.subject_id = subject_id
        self.image_path = image_path

    def __repr__(self):
        return "<Card: '{}'>".format(self.name)

