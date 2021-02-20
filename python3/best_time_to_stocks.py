from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buying_price = 2**31
        max_profit = 0
        for price in prices:
            if price < min_buying_price:
                min_buying_price = price
            else:
                max_profit = max(price-min_buying_price, max_profit)
        return max_profit