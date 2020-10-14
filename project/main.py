from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user
main = Blueprint('main', __name__)

@main.route('/')
def homepage():
    return render_template('homepage.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username = current_user.name)