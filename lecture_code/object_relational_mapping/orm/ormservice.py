from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from sqlalchemy.sql import exists

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' # memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    dob = db.Column(db.String(10), unique=False)

    def __init__(self, username, email, dob):
        self.username = username
        self.email = email
        self.dob = dob

    def __repr__(self):
        return '<User %r>' % self.username

def init_db():
    """Initializes the database."""
    db.create_all()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/createuser/<name>')
def create_user(name=None):
    exist = db.session.query(exists().where(User.username == name)).scalar()
    if exist:
        return jsonify(
            success=False,
            error={'code':0, 'message': "exists"}
        )
    else:
        admin = User(name, name + '@foomail.com', '15/02/15')
        db.session.add(admin)
        db.session.commit()
        return jsonify(
            success=True,
            error={}
        )

@app.route('/listusers')
def list_users():
    """
    {
    "success": true/false,
    "users": { id: username, id:username}
    "error": {
        "code": 123,
        "message": "An error occurred!"
        }
    }
    """
    l = db.session.query(User).all()
    l = [i.username for i in l]
    return jsonify(
        success=True,
        users=l
    )

if __name__ == "__main__":
    app.run()