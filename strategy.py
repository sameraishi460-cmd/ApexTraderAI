def calculate_signal(ema_fast, ema_slow, rsi):
    """
    حساب إشارة التداول باستخدام EMA + RSI
    """

    if ema_fast > ema_slow and rsi < 70:
        return "BUY"

    elif ema_fast < ema_slow and rsi > 30:
        return "SELL"

    else:
        return "WAIT"


def risk_management(balance, risk_percent):
    """
    حساب حجم المخاطرة
    """

    risk_amount = balance * (risk_percent / 100)

    return risk_amount


def trade_plan(balance, price, risk_percent):
    """
    خطة تداول بسيطة
    """

    risk = risk_management(balance, risk_percent)

    stop_loss = price * 0.98
    take_profit = price * 1.04

    return {
        "risk": risk,
        "stop_loss": stop_loss,
        "take_profit": take_profit
    }
