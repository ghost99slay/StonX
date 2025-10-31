from dataclasses import dataclass
from pandas import DataFrame


@dataclass
class Asset:
    ticker: str
    ohlcv_data: DataFrame
    expected_return: float
    standard_deviation: float