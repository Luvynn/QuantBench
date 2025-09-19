def calculate_position_size(balance, price, risk_per_trade=0.01):
    risk_amount = balance * risk_per_trade
    position_size = risk_amount / price
    return round(position_size, 5)
