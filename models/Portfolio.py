from random import random

from yfinance import ticker
from services.CorrelationMatrixGenerator import CorrelationMatrixGenerator
from models.Asset import Asset

class Portfolio:
    def __init__(self, tickers) -> None:
        self.tickers = [str(ticker).upper() for ticker in tickers]

        self.weights = []
        self._generate_random_weights()

        self._correlation_matrix_generator = CorrelationMatrixGenerator()
        self.correlation_matrix = self._correlation_matrix_generator.GenerateMatrix(self.tickers)

        self.assets = [Asset(ticker) for ticker in tickers]
        
        self.risk = self._portfolio_risk()
        self.expected_return = self._portfolio_expected_return()

        self.sharpe_ratio = self._sharpe_ratio()

    def __repr__(self) -> str:
        return f"Portfolio:\n{self.tickers}\n{self.weights}\nSharpe Ratio: {self.sharpe_ratio}"
        
    def _generate_random_weights(self):
        pre_normalized_weights = [random() for _ in self.tickers]
        self.weights = [x / sum(pre_normalized_weights) for x in pre_normalized_weights]
    
    def _portfolio_risk(self):
        n = len(self.weights)
        portfolio_variance = 0

        for i in range(n):
            for j in range(n):
                try:
                    contribution = self.weights[i] * self.weights[j] * self.assets[i].risk * self.assets[j].risk * self.correlation_matrix[self.assets[i].ticker][self.assets[j].ticker]
                    portfolio_variance += contribution
                except KeyError as e:
                    print(f"Error calculating corr matrix on assets: {self.tickers[i]}{self.tickers[j]}")
                    print(self.tickers)

        return portfolio_variance ** 0.5

    def _portfolio_expected_return(self):
        expected_returns = 0

        for i, asset in enumerate(self.assets):
            expected_returns += asset.expected_return * self.weights[i]

        return expected_returns

    def _sharpe_ratio(self, risk_free_rate=0.041):
        return (self.expected_return - risk_free_rate) / self.risk