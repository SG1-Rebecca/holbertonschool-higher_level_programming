from flask import Flask, jsonify, request

users = {"john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
}}

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
def user(username):
    """
    Returns the full object corresponding to the provided username
    """
    user = users.get(username.lower())

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add the new user to the users dictionary using username as the key.
    """
    user_data = request.get_json()
    username = user_data.get("username")

    if username is None:
        return jsonify({"error": "Invalid JSON"}), 400

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }), 201


if __name__ == "__main__":
    app.run()
