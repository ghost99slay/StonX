import matplotlib.pyplot as plt
import mplfinance as mpf
from pandas import DataFrame

from DataFetcher import DataFetcher

class Grapher:
    plt.figure(figsize=(12,6))

    def plot_closing_prices(self, ohlcv_data: DataFrame):
        plt.plot(ohlcv_data.index, ohlcv_data['Close'].values)
        plt.xlabel('Date')
        plt.ylabel('Closing Price ($)')
        plt.title('Stock Price Over Time')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    def plot_candlesticks(self, ohlcv_data: DataFrame):
        mpf.plot(ohlcv_data, 
             type='candle',           # 'candle' for candlesticks, 'ohlc' for OHLC bars
             style='charles',         # Style: 'charles', 'yahoo', 'nightclouds', etc.
             volume=True,             # Show volume subplot
             title='Stock Price',
             ylabel='Price ($)',
             ylabel_lower='Volume')

test_data_fetcher = DataFetcher()
aapl_ohlcv_data = test_data_fetcher.get_ohlcv_data('aapl', '2020-01-01')

test_grapher = Grapher()
test_grapher.plot_closing_prices(aapl_ohlcv_data)
test_grapher.plot_candlesticks(aapl_ohlcv_data)
