from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🚀 MertMart Flask App Running on ECS Fargate</h1>
    <p>Environment: Dev</p>
    <p>Container Hostname: {os.uname().nodename}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
