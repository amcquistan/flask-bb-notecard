from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from models import User


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])
    

class RegisterForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])

