from flask import  render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app , db, bcrypt
from flask_login import login_user, current_user, logout_user

posts = [

    {
        'author': 'Chitesh',
        'title' : 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'October 7, 2020'  
    },

    {
        'author': 'Chandan',
        'title' : 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'October 8, 2020'  
    }
]

@app.route('/')
def homeFunc():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


@app.route('/register', methods=['GET', 'POST'])
def register() :
    if current_user.is_authenticated:
        return redirect(url_for('homeFunc'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email=form.email.data, password = hashed_pwd)
        db.session.add(user)
        db.session.commit()

        flash('your account has been created! You are now able to login in', 'success')
        
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homeFunc'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('homeFunc'))
        else:
            flash('Login Unsuccessful. Please check email and password ', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout() :
    logout_user()
    return redirect(url_for('homeFunc'))