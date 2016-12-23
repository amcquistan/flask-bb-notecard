
from flask import render_template, url_for, Blueprint, redirect, request, flash, session
from flask_login import login_required, current_user
from ..models import db, User
from ..forms import SubjectForm

subject_bp = Blueprint(
    'subject',
    __name__,
    url_prefix = '/subject'
)


@subject_bp.route('/')
@login_required
def index():
    return render_template('subject/index.html')


@subject_bp.route('/<int:id>')
@login_required
def view(id):
    return render_template('subject/view.html')
    

@subject_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    return render_template('subject/create.html')


@subject_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit():
    return render_template('subject/edit.html')






