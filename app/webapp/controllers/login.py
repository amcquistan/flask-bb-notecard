from flask import render_template, url_for, Blueprint, redirect, request, flash, session
from flask_login import login_user, logout_user
from ..models import db, User
from ..forms import LoginForm, RegisterForm

login_bp = Blueprint(
    'login',
    __name__,
    url_prefix = ''
)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            username = form.username.data
        ).one()
        login_user(user, remember=form.remember.data)
        flash('You have been logged in.', category='success')
        return redirect(url_for('home.home'))

    return render_template('login/login.html', form=form)


@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user.  Please login.', category='success')
        return redirect(url_for('.login'))
    
    return render_template('login/register.html', form=form)
    

@login_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('You are now logged out.', category='success')
    return redirect(url_for('home.home'))
    
