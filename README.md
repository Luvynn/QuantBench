# QuantBench

A modular crypto trading framework for **live trading** and **backtesting**, powered by the **Binance API**.  
It comes with built-in strategies such as **RSI**, **MACD**, and **SMA crossover**, plus risk management tools for safer trading.

---

## Features
- Live trading with Binance API (REST + WebSocket)  
- Backtesting engine with performance metrics (PnL, Sharpe ratio, drawdowns)  
- Risk management: position sizing, stop-loss, take-profit  
- Modular strategy design – plug in your own algorithms easily  
- Dockerized deployment for production-ready environments  

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/QuantBench.git
cd QuantBench

2. Add API keys

Edit config.py and add your Binance API key and secret:

API_KEY = "your_api_key"
API_SECRET = "your_api_secret"

3. Install dependencies
pip install -r requirements.txt

4. Run live trading
python strategies/rsi_bot.py

5. Run backtests
python backtest.py

Example Workflow

Subscribe to real-time candlestick data via WebSocket

Run your chosen strategy (e.g., RSI > 70 → Sell, RSI < 30 → Buy)

Apply risk rules (stop-loss, position sizing)

Place orders via Binance REST API or simulate trades via backtesting

🛠 Roadmap

Planned improvements:

Multi-exchange support (Kraken, Coinbase, etc.)

Portfolio tracking dashboards

More strategies (Bollinger Bands, VWAP, momentum-based)

Enhanced backtester with historical tick-level data

Machine learning–driven signal generation

⚠️ Disclaimer

This project is for educational purposes only.
Trading cryptocurrencies involves significant risk. Use at your own discretion.
