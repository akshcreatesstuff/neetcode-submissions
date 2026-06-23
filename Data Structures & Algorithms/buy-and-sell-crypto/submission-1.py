class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        maxProfit = 0
        for price in prices:
            buy = min(price, buy)
            profit = price - buy
            maxProfit = max(profit, maxProfit)
        return maxProfit

            



        