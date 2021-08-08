from flask import Flask  # Flask class

app = Flask(__name__)


@app.route("/")  # these are decorators
@app.route("/home")
def hello():
    return "<h1> *-HOME PAGE-* </h1>"


@app.route("/about")
def about():
    return "ABOUT PAGE"


# most of the time we will be using
# export FLASK_APP='main.py'
# flask run
if __name__ == '__main__':  # useful when we use direct run
    app.run(debug=True)
