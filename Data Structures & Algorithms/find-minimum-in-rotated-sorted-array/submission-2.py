class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        U: we are returning the min number in nums in O(log n)
            I: int list
            O: int
            C:
            E: [4] -> 4

        M: Binary
            [3,4,5,6,1,2]  output: 1
             l
                     m
                        r
            mid = (l + r) // 2 = 5//2 = 2
            
            if nums[l] < nums[r]:
                min_num = nums[l]
            else:
                min_num = nums[r]

        [4,5,0,1,2,3]
         l
             r
        if len(nums) is 1: return nums

        l, r = 0, 1

        while r < len(s):
            if nums[l] > nums[r]:
                return nums[r]
            r += 1
        return nums[0]
        '''
        if len(nums) == 1: 
            return nums[0]

        l, r = 0, 1

        while r < len(nums):
            if nums[l] > nums[r]:
                return nums[r]
            r += 1
        return nums[0]
