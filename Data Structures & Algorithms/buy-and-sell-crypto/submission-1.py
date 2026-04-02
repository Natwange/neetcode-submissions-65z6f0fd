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
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        
        return maxP
        



