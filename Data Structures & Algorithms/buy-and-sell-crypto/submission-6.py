class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        profit = 0

        for price in prices:
            buy = min(buy, price)
            profit = price - buy
            max_profit = max(profit, max_profit)
        return max_profit