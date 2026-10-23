class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        U: return shortest LEN of subarray with sum>=target, if no such len, return 0
            I: int array nums, int target
            O: int
            C: subarray sum must be >= target for len to qualify
            E:

        M: Sliding window
            target = 10, nums = [2,1,5,1,5,3]  sum = 11, res = 3
                                     l
                                         r
        '''
        n, l = len(nums), 0
        res, sub_sum = float('inf'), 0

        for r in range(n):
            sub_sum += nums[r]
            while sub_sum >= target:
                res = min(res, r-l+1)
                sub_sum -= nums[l]
                l += 1
                    
        if res == float('inf'): return 0     
        else: return res
