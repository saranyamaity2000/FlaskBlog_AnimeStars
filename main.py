from flask import Flask, render_template

app = Flask(__name__)

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
        'date': 'Aug 20, 2021'
    }
]


@app.route("/")  # these are decorators
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html' , title='about')


# most of the time we will be using
# export FLASK_APP='main.py'
# flask run
if __name__ == '__main__':  # useful when we use direct run
    app.run(debug=True)
