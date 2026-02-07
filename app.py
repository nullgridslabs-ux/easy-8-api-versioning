# easy-8-api-versioning/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/health")
def health():
    return "ok"

@app.route("/api/v1/admin/stats")
def v1():
    # BUG: missing auth in v1
    return jsonify({"users":123,"flag":FLAG})

@app.route("/api/v2/admin/stats")
def v2():
    return jsonify({"error":"admin only"}),403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
