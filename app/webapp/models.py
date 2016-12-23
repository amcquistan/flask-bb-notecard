from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    subjects = db.relationship('Subject', backref='subject', lazy='dynamic')

    def __init__(self, username, password=None):
        self.username = username
        if password:
            self.password = password
        
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
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    
    def __init__(self, name, description, subject_id, image_path=None):
        self.name = name
        self.description = description
        self.subject_id = subject_id
        self.image_path = image_path

    def __repr__(self):
        return "<Card: '{}'>".format(self.name)

