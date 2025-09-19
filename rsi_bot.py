import websocket, json, talib, numpy, logging, time
import config
from binance.client import Client
from binance.enums import *
from strategies import rsi
from risk import calculate_position_size

logging.basicConfig(filename="trade_log.log", level=logging.INFO)

SOCKET = "wss://stream.binance.com:9443/ws/ltcusdt@kline_1m"
TRADE_SYMBOL = "LTCUSDT"

closes = []
in_position = False
balance = config.START_BALANCE

client = Client(config.API_KEY, config.API_SECRET)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        logging.info(f"Placing order: {side} {quantity} {symbol}")
        return client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        logging.error(f"Order failed: {e}")
        return None

def on_message(ws, message):
    global closes, in_position, balance
    json_message = json.loads(message)
    candle = json_message["k"]
    if candle["x"]:
        closes.append(float(candle["c"]))
        signal = rsi.generate_signal(closes)
        if signal == "BUY" and not in_position:
            qty = calculate_position_size(balance, closes[-1])
            order(SIDE_BUY, qty, TRADE_SYMBOL)
            in_position = True
        elif signal == "SELL" and in_position:
            qty = calculate_position_size(balance, closes[-1])
            order(SIDE_SELL, qty, TRADE_SYMBOL)
            in_position = False

def on_open(ws):
    logging.info("Opened connection")

def on_close(ws):
    logging.info("Closed connection")

if __name__ == "__main__":
    while True:
        try:
            ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
            ws.run_forever()
        except Exception as e:
            logging.error(f"WebSocket error: {e}")
            time.sleep(5)
