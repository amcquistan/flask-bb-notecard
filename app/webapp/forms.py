from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from models import User


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])
    remember = BooleanField('Remember Me')
    
    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if validators do not pass
        if not check_validate: 
            return False

        # does user exists?
        user = User.query.filter_by(
            username=self.username.data
        ).first()
        if not user:
            self.user.errors.append('Invalid username.')
            return False

        # do the passwords match?
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid password.')
            return False
        
        return True


class RegisterForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])


class SubjectForm(Form):
    name = StringField('Subject', [DataRequired(), Length(min=3)])
    description = StringField('Description', [DataRequired(), Length(min=10)])
    
