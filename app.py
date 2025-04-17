import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Test depuis le cloud pour le cas pratique 3IL3 !"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render fournit le port dans cette variable
    app.run(host="0.0.0.0", port=port)
