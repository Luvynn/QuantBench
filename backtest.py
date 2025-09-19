import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from strategies import rsi, macd, sma
from risk import calculate_position_size

def run_backtest(prices, strategy, starting_balance=1000):
    balance = starting_balance
    position = 0
    trade_log = []

    for i in range(len(prices)):
        signal = strategy.generate_signal(prices[:i+1])
        if signal == "BUY" and position == 0:
            qty = calculate_position_size(balance, prices[i])
            position = qty
            balance -= qty * prices[i]
            trade_log.append((i, "BUY", prices[i], balance))
        elif signal == "SELL" and position > 0:
            balance += position * prices[i]
            trade_log.append((i, "SELL", prices[i], balance))
            position = 0

    final_balance = balance + position * prices[-1]
    print(f"Final balance: {final_balance:.2f}")
    return trade_log, final_balance

if __name__ == "__main__":
    # Example synthetic data
    prices = np.linspace(50, 150, 200) + np.random.normal(0, 5, 200)
    trade_log, final_balance = run_backtest(prices, strategy=rsi, starting_balance=1000)

    df = pd.DataFrame(trade_log, columns=["Index", "Action", "Price", "Balance"])
    df.to_csv("results/backtest_results.csv", index=False)
    plt.plot(prices, label="Price")
    plt.scatter(df["Index"], df["Price"], c=(df["Action"]=="BUY").map({True:"g",False:"r"}))
    plt.legend()
    plt.savefig("results/backtest_plot.png")
    plt.close()
