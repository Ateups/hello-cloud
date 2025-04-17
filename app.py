from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour depuis le cloud avec Render 🌥️ !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
