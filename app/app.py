from flask import Flask, jsonify
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Abhay's AWS CI/CD Automation Project",
        "status": "Application is running successfully",
        "hostname": socket.gethostname(),
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)