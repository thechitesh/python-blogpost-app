from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/home')
def hello():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)