from . import bp as users
from app import db, mail
from .email import send_password_reset_email
from flask import render_template, request, redirect, url_for, flash
from .forms import UserForm, LoginForm, UserUpdateForm, ResetPasswordForm, ResetPasswordRequestForm
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from flask_mail import Message 

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for(('main.index')))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect Username and/or Password. Please check your credentials and try again!', 'danger')
            return redirect(url_for('users.login'))
        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in!', 'warning')
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)
    
@users.route('/.logout')
def logout():
    logout_user()
    flash('You are now logged out!', 'success')
    return redirect(url_for('main.index'))
    
@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('You have successfully reset your password!','success')
        return redirect(url_for('users.login'))
    return render_template('reset_password.html', form=form)
    
@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated():
        return redirect(url_for('main.index'))
    title = 'Register'
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)).all()
        if existing_user:
            flash('Looks like this account already exists. Please try another username and password and try again.', 'danger')
            return redirect(url_for('users.register'))
        new_user = User(username, password, email, address, city, state, zip)
        db.session.add(new_user)
        db.session.commit()
        
        msg = Message("Thank you for registering with us", recipients=[email])
        msg.body = "We appreciate your support - stay tuned..."
        mail.send(msg)
        flash("Thank you for registering with us!", 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

@users.route('/user/update', methods=['GET', 'POST'])
@login_required
def user_update():
    user = User.query.get_or_404(current_user.id)
    title = f"Update {user.username} - update"
    if user.id !=current_user.id:
        flash("You cannot update another user's account", 'danger')
        return redirect(url_for('main.index'))
    form = UserUpdateForm(user.username, user.email)
    if request.nethod == 'POST' and form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.address = form.address.data
        user.city = form.city.data
        user.state = form.state.data
        user.zip = form.zip.data
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('user_update.html', title=title, form=form, user=user)