import logging

import pandas as pd

from src.performance_matrix.base_performance_matrix import BasePerformanceMatrix
from src.performance_matrix.return_matrix.percentage_change import PercentageChange


class OmegaRatio(BasePerformanceMatrix):
    def __init__(self, stock_data: pd.DataFrame, market_data: pd.DataFrame = None, risk_free_rate: float = 0.0,
                 threshold: float = 0.0):
        super().__init__(stock_data)
        self.risk_free_rate = risk_free_rate
        self.market_data = market_data
        self.threshold = threshold

    def calculate(self):
        try:
            returns = PercentageChange(self.stock_data).calculate()
            gains = returns[returns > self.threshold] - self.threshold
            losses = self.threshold - returns[returns < self.threshold]
            return gains.sum() / losses.sum()
        except Exception as e:
            logging.error("OmegaRatio failed with error={}".format(e))
            return str(e)
