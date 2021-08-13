from main import app


# most of the time we will be using
# export FLASK_APP='run.py'
# flask run
if __name__ == '__main__':  # useful when we use direct run
    app.run(debug=True)
