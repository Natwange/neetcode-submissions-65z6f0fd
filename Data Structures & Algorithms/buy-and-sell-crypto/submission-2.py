class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Understand: find maximum profit you can gain from buying and selling stock
        Input: int array prices
        Output: int profit

        Plan:
        l,r
        maximum = 0
        loop through list:
            if nums[r] < nums[l]:
                l + 1
            else:
                num

        Implement:
        """   
        min_buy_price = float('inf')
        max_profit = 0

        for price in prices:
            min_buy_price = min(min_buy_price, price)
            max_profit = max(max_profit, price - min_buy_price)

        return max_profit



