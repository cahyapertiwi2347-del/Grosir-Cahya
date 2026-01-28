from flask import Flask, render_template, request, jsonify

try:
    from flask_cors import CORS
except ImportError:
    # Biar tetap jalan walau flask_cors belum terinstall
    CORS = None

from core import get_bot_reply

app = Flask(__name__)

# Izinkan request dari origin manapun (untuk development)
if CORS:
    CORS(app)


@app.route("/")
def index():
    # kirim dummy user supaya UI chat langsung muncul
    return render_template("index.html", user="Pengunjung")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    reply = get_bot_reply(user_message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    # debug=True agar mudah melihat error
    app.run(debug=True)
