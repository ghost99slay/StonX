# from services.StockListFetcher import StockListFetcher
from numpy import test
from models.Portfolio import Portfolio

# tickers = StockListFetcher.get_sp500_tickers()
# print(tickers)


test_portfolio = Portfolio(['k', 'pg'])
print(test_portfolio)