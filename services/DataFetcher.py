import pandas as pd
import yfinance as yf
from datetime import datetime

class DataFetcher:

    def get_ohlcv_data(self, ticker: str, start: str, end=datetime.now()):
        data = yf.download(ticker, start=start, end=end)
        
        # Flatten MultiIndex columns if they exist
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        
        return data

test_data_fetcher = DataFetcher()
print(test_data_fetcher.get_ohlcv_data('aapl', '2020-01-01'))