# easy-8-api-versioning/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)
FLAG = os.environ.get("FLAG","CTF{dev}")

@app.route("/")
def index():
    return """
<h2>Admin Statistics API</h2>
<p>Versioned admin reporting service.</p>
<ul>
<li>GET /api/v1/admin/stats</li>
<li>GET /api/v2/admin/stats</li>
<li>GET /health</li>
</ul>
"""

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
