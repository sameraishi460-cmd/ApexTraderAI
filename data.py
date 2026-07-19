import requests


def get_market_data():
    try:
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=100"

        response = requests.get(url, timeout=10)

        candles = response.json()

        closes = []

        for candle in candles:
            closes.append(float(candle[4]))

        return closes

    except Exception as e:
        print(e)
        return []
