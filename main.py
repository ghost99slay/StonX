from models.Asset import Asset
from services.StockListFetcher import StockListFetcher

tickers = StockListFetcher.get_sp500_tickers()

assets = []

for ticker in tickers:
    asset = Asset(ticker)
    assets.append(asset)

for asset in assets:
    print(asset.ticker)
    print(asset.risk)
    print(asset.expected_return)
    print('\n')