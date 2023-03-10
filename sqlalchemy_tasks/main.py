from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.department import Department


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    return user


def main():
    db_session.global_init('db/blogs.db')
    session = db_session.create_session()
    dp = session.query(Department).filter(Department.id == 1).first()
    users_id = [int(p) for p in dp.members.split(', ')]
    for u_id in users_id:
        hours = 0
        for i in session.query(Jobs).all():
            if str(u_id) in i.collaborators or u_id == i.team_leader:
                hours += i.work_size
        if hours > 10:
            print(' '.join(session.query(User.surname, User.name).filter(User.id == u_id).first()))


if __name__ == '__main__':
    main()
