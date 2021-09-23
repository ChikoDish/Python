from flask import Flask

app = Flask(__name__)


@app.route('/about')
@app.route('/')

def home():
    return "<h1>Hello World</h1>"

def about():
    return "<h1>About</h1>"

if __name__ == '__main__':
    app.run(debug=True)
