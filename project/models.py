from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    patronymic = db.Column(db.String(500))
    password_hash = db.Column(db.String(10000))

    # password = db.Column(db.String(100))
    def __init__(self, name=None, email=None, lastname=None,
                 patronymic=None, password_hash=None):
        self.email = email
        self.name = name

        self.lastname = lastname
        self.patronymic = patronymic
        self.password_hash = password_hash

    def __repr__(self):
        return '<User %r>' % (self.name)




"""
from sqlalchemy import Column, Integer, String
from project.database import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


from project.database import init_db
from project.database import db_session
from project.models import User

if __name__ == '__main__':
    init_db()
    db_session.add(User(name='adminulumba', email='adminsobaka@gmail.com'))
    db_session.commit()
    db_session.remove()
"""
