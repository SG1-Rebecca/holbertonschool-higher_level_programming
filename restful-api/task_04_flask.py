#!/usr/bin/python3
"""
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    """
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def serving_json_data():
    """
    Return a list of all the usernames stored in the API.
    """
    return jsonify(users)

@app.route("/status")
def status():
    """
    Return OK status.
    """
    return jsonify({"status": "OK"}), 200

@app.route("/users/<string:username>")
def usernames(username):
    """
    Return the full object corresponding to the provided username
    """
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404



if __name__ == "__main__": 
    app.run()
    