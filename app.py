from flask import Flask, render_template, jsonify
from market import get_btc_price

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():
    price = get_btc_price()

    return jsonify({
        "bot": "ONLINE",
        "price": price,
        "signal": "WAITING"
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
