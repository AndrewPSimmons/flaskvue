from flask import Flask, render_template, jsonify, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import exists
from flask_cors import CORS
from random import *
from datetime import datetime
import ast
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist",
            )

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    """
    ID
    FirstName
    LastName
    Username
    EmailAddress
    Password/Password info (idk exactly how to secure passwords yet)
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/createAccount', methods=["POST"])
def create_user():
    print("REQUEST MADE IT THIS FAR FROM createAccount")
    request_data = ast.literal_eval(request.get_data().decode('utf-8'))
    print("====request_data: ", request_data)
    print(request_data["first_name"])
    first_name = request_data["first_name"]
    last_name = request_data["last_name"]
    email = request_data["email"]
    username = request_data["username"]
    password = request_data["password"]

    user = User.query.filter_by(email_address=email).first()

    if user:
        return '{"response": {"type": "error", "message": "email already in use"}}'

    new_user = User(first_name=first_name, last_name=last_name,
                    email_address=email, username=username, password=password)

    db.session.add(new_user)
    db.session.commit()

    return '{"response": {"type": "success", "message": "User created"}}'


@app.route('/session')
def show_session():
    session_data = {}
    for key in session:
        session_data[key] = session[key]
    return session_data


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/api/loggedin')
def isLoggedIn():
    logged_data = {
        'loggedin': session["is_logged_in"]
    }
    return jsonify(logged_data)


@app.route('/logout', methods=["POST"])
def logout():
    session["is_logged_in"] = False
    return url_for("catch_all")

# GIT SHANGEs
@app.route('/api/loggedUser')
def logged_user():
    return session["logged_user"]


@app.route('/api/loginValidator', methods=["POST"])
def validate_login():
    print("in loginValidator")
    rawdata = request.get_data()
    data = ast.literal_eval(rawdata.decode('utf-8'))
    # print session.query(exists().where(User.email == '...')).scalar()
    print(data)
    if "is_logged_in" not in session:
        session["is_logged_in"] = False
    post_username = data["username"]
    post_password = data["password"]
    print(f"======PASSWORD: {post_password} USERNAME: {post_username}")
    print(db.session.query(exists().where(
        User.username == f'{post_username}')).scalar())
    print(db.session.query(exists().where(
        User.password == f'{post_password}')).scalar())
    if(db.session.query(exists().where(User.username == f'{post_username}')).scalar() and db.session.query(exists().where(User.password == f'{post_password}')).scalar()):
        print("IN THE IF")
        session["is_logged_in"] = True
        session["logged_user"] = post_username
        response_message = {"login_status": "Success"}
    else:
        session["is_logged_in"] = False
        response_message = {"login_status": "Failure"}
    print("AFTER RTHE IF")
    response = {
        'loggedin': session["is_logged_in"],
        'response': response_message
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


"""
@app.route('/secure/<afile>')
def secure(afile):
    return f"<p>THIS IS SECURE {afile} </p>"
"""


if __name__ == "__main__":
    app.run(debug=True)
