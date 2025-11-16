from typing import Optional

from common import StockType


class Stock:
    def __init__(
            self,
            symbol: str,
            stock_type: StockType,
            last_dividend: float,
            par_value: float,
            fixed_dividend: Optional[float] = None
    ):
        self.symbol = symbol
        self.stock_type = stock_type.value
        self.last_dividend = last_dividend
        self.par_value = par_value
        self.fixed_dividend = fixed_dividend

    def dividend_yield(self, price: float) -> float:
        if price <= 0:
            raise ValueError("Price must be > 0.")

        if self.stock_type == StockType.Common.value:
            return self.last_dividend / price
        else:  # PREFERRED
            return (self.fixed_dividend * self.par_value) / price

    def pe_ratio(self, price: float) -> float:
        dy = self.dividend_yield(price)
        if dy == 0:
            raise ValueError("Dividend yield is zero → cannot compute P/E ratio.")
        return price / dy

    def __str__(self):
        return self.symbol

