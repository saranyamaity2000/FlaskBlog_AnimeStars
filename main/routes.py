from flask import render_template, url_for, flash, redirect
from main.forms import RegistrationForm, LoginForm
from main.models import User, Post
from main import app


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')  # we have used f string for ease
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in Unsuccessful! Kindly check your Email and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)