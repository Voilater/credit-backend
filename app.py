from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = "applications.json"

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

@app.route("/applications", methods=["GET"])
def get_applications():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/applications", methods=["POST"])
def add_application():
    new_app = request.json
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    data.append(new_app)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return jsonify({"status": "success", "message": "Application added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
