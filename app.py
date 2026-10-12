
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS DevOps Project</h1>
    <p>My application is running successfully!</p>
    <p>Built with Python and Flask.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "aws-devops-project",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
