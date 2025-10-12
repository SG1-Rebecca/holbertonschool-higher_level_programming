from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Return a string message
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def serving_json_data():
    """
    Return a list of all the usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Return OK status.
    """
    return "OK", 200


@app.route("/users/<string:username>")
def get_user_by_username(username):
    """
    Return the full object corresponding to the provided username
    """
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    """
    Add the new user to the users dictionary.
    """
    user_data = request.get_json()
    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data}), 201


if __name__ == "__main__":
    app.run()
