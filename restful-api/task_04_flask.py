#!/usr/bin/python3
"""
"""
from flask import Flask, jsonify

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


if __name__ == "__main__": 
    app.run()
    