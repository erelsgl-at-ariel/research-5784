# This time, we design the "account update" page, and allow to upload a new profile picture.

import os
import secrets
from PIL import Image  # To resize the uploaded profile pics
from flask import render_template, url_for, flash, redirect ,request
from flask_example import app, db, bcrypt
from flask_example.forms import RegistrationForm, LoginForm , UpdateAccountForm
from flask_example.models import User , Post
from flask_login import login_user , current_user , logout_user ,login_required

users = [
    {'name': 'Joee Javany',
    'email': 'joo@example.com',
    'phone': '111-1111'},
    {'name': 'Tom Pythonovitch',
    'email': 'python_is_coool@example.com',
    'phone': '222-2222'},
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html' , users = users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)  # random name with 16 digits (8 hex numbers)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    img_file = Image.open(form_picture)
    img_file.thumbnail(output_size)
    img_file.save(picture_path)

    return picture_fn

@app.route("/account" ,methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():  # POST
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.profile_img = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET': # GET: Automatically put the current username and email in the form fields.
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static' , filename= f'profile_pics/{current_user.profile_img}')
    return render_template('account.html', title='Account', image_file = image_file , form = form)

