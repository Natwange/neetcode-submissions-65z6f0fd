class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)  == 1:
            return 0

        min_buy_price = float('inf')
        max_profit = 0

        for num in prices:
            min_buy_price = min(min_buy_price, num)
            max_profit = max(max_profit, num - min_buy_price)
        return max_profit