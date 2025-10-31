from dataclasses import dataclass
from models import Asset

weight = float

@dataclass
class Portfolio:
    assets: {Asset: weight}
    starting_balance: float
    expected_return: float
    standard_deviation: float