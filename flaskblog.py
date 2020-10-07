from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
#scret key is added to protect agains csrf other hacks
app.config['SECRET_KEY'] = '8feff63c1e248b6b1bd50e1efff2fca1'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('homeFunc'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'password' :
            flash('You have been successfully logged in !', 'success')
            return redirect(url_for('homeFunc'))
        else :
            flash('Login Unsuccessful. Please check email and password ', 'danger')

    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)