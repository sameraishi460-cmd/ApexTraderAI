def calculate_signal(price, ema_fast, ema_slow):
    """
    حساب إشارة التداول
    """

    if ema_fast > ema_slow:
        return "BUY"

    elif ema_fast < ema_slow:
        return "SELL"

    else:
        return "WAIT"


def risk_management(balance, risk_percent):
    """
    حساب حجم المخاطرة
    """

    risk_amount = balance * (risk_percent / 100)

    return risk_amount
