import talib
import numpy as np

def generate_signal(prices):
    np_closes = np.array(prices)
    macd, signal, hist = talib.MACD(np_closes, fastperiod=12, slowperiod=26, signalperiod=9)
    if macd[-1] > signal[-1]:
        return "BUY"
    elif macd[-1] < signal[-1]:
        return "SELL"
    return None
