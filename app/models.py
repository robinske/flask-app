from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from app import db, bcrypt


class User(db.Model, UserMixin):

    ''' A user who has an account on the website. '''

    __tablename__ = 'users'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)

    def __init__(self, first_name, last_name, phone, email, confirmation, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.confirmation = confirmation
        self._password = password

    def __repr__(self):
        return '<email {}>'.format(self.email)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        try:
            return bcrypt.check_password_hash(self.password, plaintext)
        except ValueError:
            return "Invalid password"

    def get_id(self):
        return self.email
