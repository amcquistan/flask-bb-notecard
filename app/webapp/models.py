from flask_sqlalchemy import SQLAlchemy
from extensions import bcrypt
from flask_login import AnonymousUserMixin
from medea import medea, MedeaMapper

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

medea.register(User, MedeaMapper(
    'id', 'username'
))


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cards = db.relationship('Card', backref='subject', lazy='dynamic')

    def __init__(self, name, user_id, description=None):
        self.name = name
        self.description = description
        self.user_id = user_id

    # def __repr__(self):
    #     return "<Subject: '{}'>".format(self.name)

medea.register(Subject, MedeaMapper(
    'id', 'name', 'description', 'user_id'
))


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(650))
    answer = db.Column(db.String(100))
    image_path = db.Column(db.String(100))
    correct_responses = db.Column(db.Integer)
    total_views = db.Column(db.Integer)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    
    def __init__(self, title, description, answer, subject_id, image_path=None):
        self.title = title
        self.description = description
        self.answer = answer
        self.subject_id = subject_id
        self.image_path = image_path

    def __repr__(self):
        return "<Card: '{}'>".format(self.title)

medea.register(Card, MedeaMapper(
    'id', 'title', 'description', 'image_path', 'answer',
    'correct_responses', 'total_views', 'subject_id'
))
