#!/usr/bin/python3
"""
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    """
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def serving_json_data():
    """
    """
    data = users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
    return jsonify(data)


if __name__ == "__main__": app.run()