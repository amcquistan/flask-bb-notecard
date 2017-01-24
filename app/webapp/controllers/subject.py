from __future__ import print_function
from flask import render_template, url_for, Blueprint, redirect, request, flash, session, jsonify
from flask_login import login_required, current_user
from ..models import db, User, Subject, Card
from ..forms import SubjectForm
from medea import medea, MedeaMapper
from ..config import Config
from werkzeug import secure_filename
import os.path
import random

import sys

subject_bp = Blueprint(
    'subject',
    __name__,
    url_prefix = '/subject'
)


@subject_bp.route('/', methods=['GET', 'POST'])
@login_required
def subjects():
    if request.method == 'POST':
        args = request.get_json()
        s = Subject(name=args['name'], description=args['description'], user_id=current_user.id)
        db.session.add(s)
        db.session.commit()
        return jsonify(s)

    subjects = Subject.query.filter_by(user_id=current_user.id).order_by(Subject.id).all()
    return render_template('subject/index.html', subjects=subjects)


@subject_bp.route('/<int:id>', methods=['GET', 'PUT'])
@login_required
def subject(id):
    subject = Subject.query.get(id)
    if request.method == 'PUT':
        args = request.get_json()
        if args['name']:
            subject.name = args['name']
        if args['description']:
            subject.description = args['description']
        db.session.commit()

    return jsonify(subject)
    

@subject_bp.route('/<int:subject_id>/card', methods=['GET', 'POST'])
@login_required
def cards(subject_id):
    if request.method == 'POST':
        args = request.get_json()
        card = Card(args['title'], args['description'], args['answer'], subject_id)
        if args['image_path']:
            card.image_path = args['image_path']
        db.session.add(card)
        db.session.commit()
        return jsonify(card)
    
    subject = Subject.query.get(subject_id)
    cards = subject.cards.all()
    return render_template('notecard/index.html', cards=cards, subject_id=subject_id, subject=subject)


@subject_bp.route('/<int:subject_id>/card/<int:card_id>', methods=['GET', 'PUT'])
@login_required
def card(subject_id, card_id):
    card = Card.query.get(card_id)
    if request.method == 'PUT':
        args = request.get_json()
        if args['name']:
            card.name = args['name']
        if args['description']:
            card.description = args['description']
        if args['image_path']:
            card.image_path = args['image_path']
        db.session.commit()
    
    return jsonify(card)

@subject_bp.route('/<int:subject_id>/card/imageupload', methods=['POST'])
@login_required
def card_imageupload(subject_id):
    resp = {'status':'ERROR'}
    file = request.files['fileInput']
    if file and _allowed_file(file.filename):
        filename = secure_filename(file.filename)
        images_folder = Config.UPLOAD_DIR

        while True:
            file_exists = os.path.exists(images_folder + '/' + filename)
            if not file_exists:
                file.save(images_folder + '/' + filename)
                break
            else:
              random_part =  str(random.randint(1,1000))
              filename = random_part + '-' + filename

        resp['status'] = 'SUCCESS'
        resp['filepath'] = images_folder + '/' + filename

    return jsonify(resp)


def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in Config.ALLOWED_UPLOAD_EXT




