class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        U: pair of numbers with biggest difference right -> left
            I: int list
            O: int
            C:
            E: [10,8,7,5,2] -> 0
                [7] -> 0
                [2,2,2,2] -> 0
                [0,0,0] -> 0

        M: Sliding window

        P: [2] -> 0
            l
            r
                profit = 0        max_res = 0
        '''
        profit = 0
        max_res = float('-inf')
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] -prices[l]
                max_res = max(max_res, profit)

        return max_res

            


        
