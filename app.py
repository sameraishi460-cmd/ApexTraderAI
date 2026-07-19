from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/status")
def status():
    return jsonify({
        "bot": "ONLINE",
        "price": "65000",
        "signal": "BUY"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
