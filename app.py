from flask import Flask, render_template, jsonify
from market import get_btc_price
from strategy import calculate_signal
from data import get_market_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():

    price = get_btc_price()

    candles = get_market_data()

    if price is None or len(candles) < 20:
        return jsonify({
            "bot": "ONLINE",
            "price": price or 0,
            "signal": "WAIT"
        })


    # حساب متوسطات بسيطة من البيانات
    ema_fast = sum(candles[-20:]) / 20
    ema_slow = sum(candles[-50:]) / 50 if len(candles) >= 50 else sum(candles) / len(candles)


    # قيمة مؤقتة للـ RSI (سنحسبها لاحقاً)
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
