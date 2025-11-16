import random

from Exchange import Exchange
from Stock import Stock
from Trade import Trade
from common import StockType
from datetime import datetime, timedelta

if __name__ == '__main__':
    market = Exchange()


    market.add_stock(Stock("TEA", StockType.Common, last_dividend=0, par_value=100))
    market.add_stock(Stock("POP", StockType.Common, last_dividend=8, par_value=100))
    market.add_stock(Stock("ALE", StockType.Common, last_dividend=23, par_value=60))
    market.add_stock(Stock("GIN", StockType.Preferred, last_dividend=8, par_value=100, fixed_dividend=0.02))
    market.add_stock(Stock("JOE", StockType.Common, last_dividend=13, par_value=250))

    givenstocksymbol = "POP"
    givenprice = 10
    givenstock = market.getalllistedStocks().get(givenstocksymbol)

    print(f"2.a.i Dividend Yield of {givenstock}: {givenstock.dividend_yield(givenprice)}")
    print(f"2.a.ii P/E Ratio of {givenstock}: {givenstock.pe_ratio(givenprice)}")

    # Add random trades (Aggregation)
    for i in range(200):
        price = round(random.gauss(100., 5.), 2)
        indicator = random.choice(['B', 'S'])
        quantity = round(random.gauss(100., 10.), 0)
        symbol = random.choice(list(market.getalllistedStocks().keys()))

        market.add_trade(quantity=quantity, indicator=indicator, price=price, symbol=symbol)

    print(f"2.a.iii all trades added successfully.")

    # Last 5 minutes VWP
    vwp = market.volume_weighted_price(
        givenstock,
        datetime.utcnow() - timedelta(minutes=5),
        datetime.utcnow()
    )
    print(f"2.a.iv Volume Weighted Price for {givenstock}: {vwp}")

    # GBCE Index
    print(f"2.b GBCE All Share Index: {market.gbce_all_share_index()}")
