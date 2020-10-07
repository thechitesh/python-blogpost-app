
#for dealing with Forms in flask
pip install flask-wtf

#Email validator error
pip install email_validator

#Database
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

