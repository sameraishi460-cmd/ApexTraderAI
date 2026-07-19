import time
from strategy import calculate_signal, risk_management

balance = 1000
risk = 1

def start_bot():
    print("🚀 ApexTrader AI Started")

    while True:
        # بيانات تجريبية مؤقتة
        ema_fast = 105
        ema_slow = 100
        price = 105

        signal = calculate_signal(
            price,
            ema_fast,
            ema_slow
        )

        risk_amount = risk_management(
            balance,
            risk
        )

        print("Price:", price)
        print("Signal:", signal)
        print("Risk:", risk_amount)

        time.sleep(60)


if __name__ == "__main__":
    start_bot()
