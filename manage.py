from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from termcolor import colored

from app import app, db, models


manager = Manager(app)

@manager.command
def initdb():
    ''' Create the Postgresql database. '''
    db.create_all()
    print(colored('The Postgresql database has been created', 'green'))


@manager.command
def dropdb():
    ''' Delete the Postgresql database. '''
    if prompt_bool('Are you sure you want to lose all your Postgresql data?'):
        db.drop_all()
        print(colored('The Postgresql database has been deleted', 'green'))


if __name__ == '__main__':
    manager.run()
