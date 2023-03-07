import datetime
from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    jobs = orm.relationship('Jobs', back_populates='user')

    def __str__(self):
        word = f'{self.surname} {self.name} {self.age} {self.position} {self.speciality} {self.email} '
        word += f'{self.hashed_password}'
        return word

    def __repr__(self):
        return str(self)