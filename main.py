from services.StockListFetcher import StockListFetcher
from numpy import test
from models.Portfolio import Portfolio



test_portfolio = Portfolio(StockListFetcher.get_sp500_tickers())
print(test_portfolio)