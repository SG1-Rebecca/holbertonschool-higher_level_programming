from flask import Flask, jsonify, request

users = {}

app = Flask(__name__)


@app.route("/")
def home():
    """
    Return a string message
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def serve_json_data():
    """
    Return a list of all the usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns OK
    """
    return "OK", 200


@app.route("/users/<string:username>", methods=["GET"])
def get_user(username):
    """
    Returns the full object corresponding to the provided username
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add the new user to the users dictionary using username as the key.
    """
    user_data = request.get_json(silent=True)

    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
