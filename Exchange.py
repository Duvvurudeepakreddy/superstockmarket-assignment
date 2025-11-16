import math
import typing
from datetime import datetime, timedelta
from typing import Optional

from Stock import Stock
from Trade import Trade


class Exchange:
    def __init__(self):
        self._listedStocks: dict[str, Stock] = {}     # Aggregation
        self.tradebook:typing.List[Trade]=[]               # Composition

    def add_stock(self, stock: Stock):
        self._listedStocks[stock.symbol] = stock

    def getalllistedStocks(self):
        return self._listedStocks

    # Volume Weighted Price
    def volume_weighted_price(self, stock: Stock,
                              starttime=datetime.min,
                              endtime=datetime.utcnow()) -> float:

        trades = self.tradebook
        num = sum(
            t.price * t.quantity
            for t in trades
            if starttime < t.timestamp < endtime and t.stocksymbol == stock.symbol
        )

        denom = sum(
            t.quantity
            for t in trades
            if starttime < t.timestamp < endtime and t.stocksymbol == stock.symbol
        ) or 1.0

        return num / denom

    # GBCE All Share Index (Geometric Mean)
    def gbce_all_share_index(self) -> Optional[float]:
        vmsp=1
        if not self._listedStocks:
            return None
        for stock in self._listedStocks.values():
            vmsp = vmsp*self.volume_weighted_price(stock)


        return vmsp ** (1 / len(self._listedStocks))


    def add_trade(self,quantity, indicator, price,symbol):
        t=Trade(quantity=quantity, indicator=indicator, price=price, symbol=symbol)
        self.tradebook.append(t)
        print(f"Trade {t} has been added")