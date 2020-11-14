
# About the App

This is blog post App, where a you can register and do a login further.
The app has different navigation bar which can take to about page and home page
There is also a side bar introduced which will show the latest post, announcements etc
The is under development and is prepared for learning python programming language.

Follow the link :- http://127.0.0.1:5000/


# Technical 
## setting up windown environment for python flask
https://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/
https://www.twilio.com/blog/how-run-flask-application

## To run the project 
- don't forget to set environment variable 
    * on cmd  :- 
        -> set FLASK_APP = run.py
        -> set FLASK_DEBUG = 1 (to make debug mode active or 0 to set it off)
        -> python3 run.py

    * windows powershell
        -> python3 run.py


### for dealing with Forms in flask
pip install flask-wtf

### Email validator error
pip install email_validator

## Database
pip install flask-sqlalchemy

- after installing the sqlalchemy we need to add configuration 
e.g. 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db = SQLAlchemy(app)

once these are done either we can create models or we can go to project directory in command line and create the empty database using below commands.

1 -> prjectdir
2 -> python
3 -> from flaskblog import db
4 -> db.create_all()

and then you can see the site.db created in the project directory

ref:- https://www.youtube.com/watch?v=cYWiDiIUxQc&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=4&ab_channel=CoreySchafer

if we have created the models then we can create the entries in db using command line as well.

5 -> from flaskblog import User, Post
6 -> user_1 = User(username='Chitesh', email='admin@admin.com', password='password')
7 -> db.session.add(user_1)
8 -> db.session.commit()

To drop everything user db.drop_all()  and then if you want to very then you have to do db.create_all() and then User.query.all() etc.

## To save the password securely we need a hashing algorithm, hence we will install
-> pip install flask-bcrypt


## install login manager
-> pip install flask-login