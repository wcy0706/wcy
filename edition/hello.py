from flask import Flask
from flask.ext.script import Manager


manager = Manager(app)
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return'<h1>Hello, %s!</h1>' % name



if __name__ == '__main__':
    app.run(debug=True)


