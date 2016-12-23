
from flask import render_template, url_for, Blueprint

home_bp = Blueprint(
    'home',
    __name__,
    url_prefix = '/home'
)


@home_bp.route('/')
def home():
    return render_template('index.html')


