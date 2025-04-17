import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour depuis le cloud avec Render 🌥️ !"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render fournit le port dans cette variable
    app.run(host="0.0.0.0", port=port)
