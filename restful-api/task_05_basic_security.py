from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the username and password.
    """
    user = users.get(username)
    if user and check_password_hash(user.get("password"), password):
        return user


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Returns a message if the user provides
    valid basic authentication credentials
    """
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run()
