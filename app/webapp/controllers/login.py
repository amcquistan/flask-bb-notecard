from flask import render_template, url_for, Blueprint, redirect, request, flash, session
from ..models import db, User
from ..forms import LoginForm, RegisterForm

login_bp = Blueprint(
    'login',
    __name__,
    url_prefix = '/login'
)


@login_bp.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user and user.password == form.password.data:
            flash('You are successfully logged in.')
            return redirect(url_for('home.home'))
        else:
            print 'Either no user or incorrect password'
            flash('Incorrect credentials.')
    else:
        print 'form did not validate'
        flash('Incorrect credentials.')
    return render_template('login/login.html', form=form)


@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user.  Please login.')
        return redirect(url_for('login.login'))
    
    return render_template('login/register.html', form=form)
    

