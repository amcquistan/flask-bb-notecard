
from flask import render_template, url_for, Blueprint, redirect, request, flash, session, jsonify
from flask_login import login_required, current_user
from ..models import db, User, Subject
from ..forms import SubjectForm
from medea import medea, MedeaMapper

subject_bp = Blueprint(
    'subject',
    __name__,
    url_prefix = '/subject'
)


@subject_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        args = request.get_json()
        print args
        s = Subject(name=args['name'], description=args['description'], user_id=current_user.id)
        db.session.add(s)
        db.session.commit()
        return jsonify(s)

    subjects = Subject.query.filter_by(user_id=current_user.id).all()
    return render_template('subject/index.html', subjects=subjects)


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






