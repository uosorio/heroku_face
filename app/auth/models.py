"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 24/05/2019

"""

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):

    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    contrato = db.Column(db.String(128), nullable=False)
    image_name = db.Column(db.String)
    csv_name = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, contrato):
        self.name = name
        self.email = email
        self.contrato = contrato

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_contrato(contrato):
        return User.query.filter_by(contrato=contrato).all()

    @staticmethod
    def get_by_count(contrato):
        return User.query.filter_by(contrato=contrato).count()

    @staticmethod
    def get_all():
        return User.query.all()
