from pandas import DataFrame
from websockets.typing import Data
import yfinance as yf
class Asset:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self.asset_data_5y = self._get_asset_data_5y(self.ticker)
        self.market_data_5y = self._get_asset_data_5y('SPY')
        self.asset_returns_5y = self._calculate_asset_returns(self.asset_data_5y)
        self.market_returns_5y = self._calculate_asset_returns(self.market_data_5y)
        self.asset_variance = self._calculate_variance(self.asset_returns_5y)
        self.market_variance = self._calculate_variance(self.market_returns_5y)

        # Probably want to change where this gets market returns from to improve performance (ie. have datamanager)
        self.covariance = self._calculate_covariance(self.asset_returns_5y, self.market_returns_5y)
        self.beta = self._calculate_beta(self.market_variance, self.covariance)
        self.risk = self._calculate_risk(self.asset_variance)
        self.expected_return = self._calculate_expected_return(risk_free_rate=0.041, beta=self.beta, erp=0.05)

    def _get_asset_data_5y(self, ticker):
        return yf.download(ticker, period='5y', interval='1d')

    def _calculate_asset_returns(self, asset_data: DataFrame):
        return asset_data['Close'].pct_change()[1:]

    def _calculate_variance(self, asset_returns:DataFrame):
        n = asset_returns.count()
        sum_of_squared_deviations = DataFrame((asset_returns - asset_returns.mean()) ** 2).sum()
        return float(sum_of_squared_deviations / (n-1))
        

    def _calculate_covariance(self, asset_returns:DataFrame, market_returns:DataFrame):
        n = asset_returns.count()
        asset_mean = asset_returns.mean()
        market_mean = market_returns.mean()

        asset_deviations = DataFrame(asset_returns - asset_mean)
        market_deviations = DataFrame(market_returns - market_mean)

        asset_deviations.columns = ['deviations']
        market_deviations.columns = ['deviations']
        cross_product = DataFrame(asset_deviations * market_deviations)
        sum_of_cross_product = cross_product.sum()[0]

        return float(sum_of_cross_product / (n-1))

    def _calculate_beta(self, market_variance, covariance):
        return covariance / market_variance

    def _calculate_risk(self, variance):
        return variance ** 0.5

    def _calculate_expected_return(self, risk_free_rate, beta, erp):
        return risk_free_rate + beta * erp

# Testing purposes
stock = Asset('aapl')
for prop, value in stock.__dict__.items():
    print(f"{prop}: {value}\n\n\n")