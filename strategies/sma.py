import talib
import numpy as np

def generate_signal(prices):
    np_closes = np.array(prices)
    sma_short = talib.SMA(np_closes, timeperiod=10)
    sma_long = talib.SMA(np_closes, timeperiod=30)
    if sma_short[-1] > sma_long[-1]:
        return "BUY"
    elif sma_short[-1] < sma_long[-1]:
        return "SELL"
    return None
