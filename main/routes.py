from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required

from main.forms import RegistrationForm, LoginForm
from main.models import User, Post
from main import app, db, bcrypt


posts = [
    {
        'author': 'Saranya Maity',
        'title': 'How to Excel in Competitive Programming',
        'content': 'Go to my Github profile github.com/saranyamaity2000',
        'date': 'Aug 9, 2021'
    },
    {
        'author': 'Swagato Bag',
        'title': 'Placed in HRC!',
        'content': 'I am very glad to say, after a lot work experience finally placed in HRC',
        'date': 'Aug 15, 2021'
    }
]


@app.route("/")  # these are decorators
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])  # Get request and POST request
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You will be able to log in', 'success')  # we have used f string for ease
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
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            flash('Log in Unsuccessful! Kindly check your Email and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')