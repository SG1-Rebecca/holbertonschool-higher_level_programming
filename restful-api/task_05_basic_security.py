from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"
              },
    "admin1": {
        "username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"
               }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the username and password for Basic Auth.
    """
    user_info = users.get(username)

    if user_info and check_password_hash(user_info["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def secure_data():
    """
    Return a message if the user is authenticated using Basic Auth.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate the user and return a JWT token if the credentials are valid.
    """
    data = request.get_json(silent=True)

    # Check if JSON data is provided
    if not data:
        return jsonify({"msg": "Missing JSON in request"}), 401

    username = data.get("username")
    password = data.get("password")

    # Check if both username and password are provided
    if not username or not password:
        return jsonify({"msg": "Missing credentials"}), 401

    user = users.get(username)

    # Check if the user exists and the password is correct
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Create a JWT token for the authenticated user
    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Return a message if the user is authenticated using JWT.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def is_admin():
    """
    Return a message if the user has an admin role.
    """
    current_user = get_jwt_identity()
    user_info = users.get(current_user)

    if user_info and user_info["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run()
