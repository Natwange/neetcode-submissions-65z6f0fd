class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        U: returning the peak element (strictly gt neigh)
        
        '''
        n = max(nums)
        for i, num in enumerate(nums):
            if num == n:
                return i
       