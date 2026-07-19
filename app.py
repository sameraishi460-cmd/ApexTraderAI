from flask import Flask, render_template, jsonify
from market import get_btc_price

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def get_signal(price):
    if price > 100000:
        return "BUY 🟢"
    elif price < 90000:
        return "SELL 🔴"
    else:
        return "WAITING 🟡"


@app.route("/status")
def status():

    price = get_btc_price()

    signal = get_signal(price)

    return jsonify({
        "bot": "ONLINE",
        "price": price,
        "signal": signal
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
