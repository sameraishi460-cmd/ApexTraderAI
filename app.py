from flask import Flask, render_template, jsonify
from market import get_btc_price
from strategy import calculate_signal

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():

    price = get_btc_price()

    if price is None:
        return jsonify({
            "bot": "ONLINE",
            "price": 0,
            "signal": "WAIT"
        })

    ema_fast = price * 1.001
    ema_slow = price

    rsi = 50

    signal = calculate_signal(
        ema_fast,
        ema_slow,
        rsi
    )

    return jsonify({
        "bot": "ONLINE",
        "price": price,
        "signal": signal
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
