# Now, we added login validation, logout route, and account page.

from flask import render_template, url_for, flash, redirect ,request
from flask_example import app, db, bcrypt
from flask_example.forms import RegistrationForm, LoginForm
from flask_example.models import User , Post
import flask_login 

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
    if flask_login.current_user.is_authenticated:     # User is already logged in - go directly to home
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated:     # User is already logged in - go directly to home
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flask_login.login_user(user, remember=form.remember.data)   # Remember that user is logged in 
            next_page = request.args.get('next') # This is activated, for example, if the user goes to the 'account' page and then redirected to the 'login' page.
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")  # New
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@flask_login.login_required  # Mark that this page can be entered only by a logged-in user
def account():
    return render_template('account.html', title='Account')
