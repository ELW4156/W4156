import flask
from flask import Flask

from lecture_code.testing.wrap_around_counter.wraparoundcounter import WrapAroundCounter

app = Flask(__name__)
app.debug = True

wac = WrapAroundCounter(10)

@app.route('/')
def hello_world():
    return 'Hello, World!!'


@app.route('/counter/<argument>')
def counter(argument):
    incremented = wac.increment(int(argument))
    return flask.jsonify({'incremented' : incremented})

if __name__ == "__main__":
    app.run()
