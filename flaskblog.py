from flask import Flask

app = Flask(__name__)


@app.route('/home')
def hello():
    return '<h1> Home Page </h2>'

@app.route('/about')
def about():
    return "<h2> About Page </h2>"


if __name__ == '__main__':
    app.run(debug=True)