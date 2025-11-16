from datetime import datetime, timedelta
class Trade:
    def __init__(self, quantity, indicator, price, symbol):
        self.timestamp = datetime.utcnow()
        self.quantity = quantity
        self.indicator = indicator.upper()
        self.price = price
        self.stocksymbol = symbol

    def __str__(self):
          s=f"TimeStamp={self.timestamp} Price={self.price}  Quantity={self.quantity} symbol={self.stocksymbol} indicator={self.indicator}"
          return s

