class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = float('inf')
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > max_profit:
                max_profit = price - buy
        return max_profit