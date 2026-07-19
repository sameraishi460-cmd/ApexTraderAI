import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    try:
        response = requests.get(url)
        data = response.json()
        return data["bitcoin"]["usd"]

    except:
        return 0
