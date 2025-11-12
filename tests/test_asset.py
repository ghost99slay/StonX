from pandas import DataFrame
import pytest

from models.Asset import Asset

def test_initialize_with_lowercase_ticker():
    asset = Asset('aapl')
    assert asset.ticker == 'AAPL'

def test_initialization_with_uppercase_ticker():
    asset = Asset('AAPL')
    assert asset.ticker == 'AAPL'

def test_initializing_gets_asset_data_dataframe():
    asset = Asset('aapl')
    assert type(asset.asset_data_5y) == DataFrame

def test_asset_data_has_OHLCV_columns():
    ticker = 'AAPL'
    asset = Asset(ticker)
    columns = list(asset.asset_data_5y.columns)
    assert columns == [('Close', ticker), ('High', ticker), ('Low', ticker), ('Open', ticker), ('Volume', ticker)]

def test_initializing_gets_market_data_dataframe():
    asset = Asset('aapl')
    assert type(asset.market_data_5y) == DataFrame

