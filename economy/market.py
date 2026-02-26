# economy/market.py
import random

class Market:
    def __init__(self):
        self.prices = {"milk": 2.0, "eggs": 1.0, "cow": 200}
        self.volatility = {"milk": 0.2, "eggs": 0.1, "cow": 0.3}

    def update_prices(self):
        for product in self.prices:
            change = random.uniform(-self.volatility[product], self.volatility[product])
            self.prices[product] += change
            self.prices[product] = max(0.1, self.prices[product])