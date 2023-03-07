from .db_session import SqlAlchemyBase
import sqlalchemy
from sqlalchemy import orm


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.String)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    user = orm.relationship('User')

    def __str__(self):
        word = f'{self.team_leader} {self.job} {self.work_size} {self.collaborators} {self.is_finished}'
        return word

    def __repr__(self):
        return str(self)