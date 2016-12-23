from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from webapp import app
from webapp.models import db, User, Subject, Card

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Subject=Subject,
        Card=Card
    )

if __name__ == '__main__':
    manager.run()


