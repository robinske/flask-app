from flask_script import Manager, prompt_bool
from termcolor import colored

from app import app, db, models


manager = Manager(app)


def make_shell_context():
    return dict(app=app)


@manager.command
def initdb():
    ''' Create the SQL database. '''
    db.create_all()
    print(colored('The SQL database has been created', 'green'))


@manager.command
def dropdb():
    ''' Delete the SQL database. '''
    if prompt_bool('Are you sure you want to lose all your SQL data?'):
        db.drop_all()
        print(colored('The SQL database has been deleted', 'green'))


if __name__ == '__main__':
    manager.run()
