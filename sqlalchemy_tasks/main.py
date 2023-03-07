from flask import Flask
from data import db_session
from data.users import User


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
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()
    session.add(add_user('Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'))
    session.add(add_user('Smith', 'Tom', 32, 'Senior', 'researching engineer', 'module_1', 'smith324397@mars.org'))
    session.add(add_user('Petrov', 'Vasya', 24, 'Middle', 'researching engineer', 'module_0', 'Vasya_top@mars.org'))
    session.add(add_user('Ivanov', 'Petya', 23, 'Junior', 'researching engineer', 'module_0', 'Vasya_loh@mars.org'))
    session.commit()


if __name__ == '__main__':
    main()
