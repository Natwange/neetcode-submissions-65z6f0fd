class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        U: 1. return index if target found, else 
           2. return the index where it would be inserted in order
            I: array of ints and int target
            O: int
            C: O(log n) time
            E: [1], 2 -> 1
               [4], 2 -> 0
        
        M: Binary Search
            nums = [-1,0,2,4,6,8], target = 5    res = 3
                           l
                           m      
                            r

        P:
        l,

        I:

        R:

        E:
        '''
        l, r = 0, len(nums) - 1
        low, up = 0, 0

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                res = l
            else:
                r = m - 1
                res = m
        return res



