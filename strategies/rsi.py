import talib
import numpy as np

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

def generate_signal(prices):
    np_closes = np.array(prices)
    if len(np_closes) < RSI_PERIOD:
        return None
    rsi = talib.RSI(np_closes, RSI_PERIOD)
    last_rsi = rsi[-1]
    if last_rsi > RSI_OVERBOUGHT:
        return "SELL"
    elif last_rsi < RSI_OVERSOLD:
        return "BUY"
    return None
