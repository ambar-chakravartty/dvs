from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from .forms import LoginForm, RegistrationForm
from . import login_manager,mongo

bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user_by_email(form.email.data)
        if user and check_password_hash(mongo.db.users.find_one({'email': form.email.data})['password'], form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('routes.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        User.insert_user(username=form.username.data, email=form.email.data, password=hashed_password)
        flash('Your account has been created!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
