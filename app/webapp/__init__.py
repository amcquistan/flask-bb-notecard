
from flask import Flask, url_for, redirect, render_template
from config import DevConfig
from models import db
from controllers.home import home_bp
from controllers.login import login_bp
from controllers.subject import subject_bp
from extensions import bcrypt, login_manager
from encoders import JSONEncoder

app = Flask(__name__)
app.config.from_object(DevConfig)
app.json_encoder = JSONEncoder
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('home.home'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html', error=error)


app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(subject_bp)


if __name__ == '__main__':
    app.run()

