from flask import Blueprint, render_template, url_for, request, redirect, \
    flash
from . import db
from .models import User
from .hash_module import hash_password, verify_password
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    # check user exists
    if not user or not verify_password(user.password_hash, password):
        flash('Введённые вами данные неверны или такого пользователя не '
              'существует')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    last_name = request.form.get('lastname')
    patronymic = request.form.get('patronymic')
    password = request.form.get('password')

    pwd_hash = hash_password(password)

    user = User.query.filter_by(email=email).first()
    print(user)
    if user:
        flash('Адрес уже зарегистрирован')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email,
                    name=name,
                    lastname=last_name,
                    patronymic=patronymic,
                    password_hash=pwd_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))
