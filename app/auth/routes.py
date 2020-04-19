from flask import render_template, redirect, url_for, request, flash
from app.auth.forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user
from app.auth import auth
from app import bcrypt, login_manager, db
from app.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if current_user.role_id != 3:
               return redirect(next_page or url_for('home'))
            else:
                return redirect(next_page or url_for('admin_panel'))
        else:
            flash('Unsuccessful Log In. Please check your email and password', 'danger')
    return render_template('auth/login.html', form=form, title="Login Page")


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        hashed_pwd = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = User(username=username, email=email,
                    password=hashed_pwd, role_id=1)

        db.session.add(user)
        db.session.commit()
        flash("Thank your for registering with us. You can now login and vote!!!")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title="Registration Page")


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
