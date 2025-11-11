from datetime import date
from dateutil.relativedelta import relativedelta

from pandas import DataFrame
import yfinance as yf


class CorrelationMatrixGenerator:
    def __init__(self):
        self.today = date.today()
        self.five_years_ago = self.today - relativedelta(years=5)

    def GenerateMatrix(self, tickers) -> DataFrame:
        data = yf.download(tickers, start=self.five_years_ago, end=self.today, auto_adjust=True)['Close'].dropna(axis=1)
        returns = data.pct_change()

        corr_matrix = returns.corr()
        return corr_matrix