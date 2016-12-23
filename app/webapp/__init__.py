
from flask import Flask, url_for, redirect, render_template
from config import DevConfig
from models import db
from controllers.home import home_bp
from controllers.login import login_bp


app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('home.home'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html', error=error)


app.register_blueprint(home_bp)
app.register_blueprint(login_bp)


if __name__ == '__main__':
    app.run()

