class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        U: return the index of target if it is found, if it's not
        found, return the index of where it would be inserted.
            I: a list
            O: int
            C: 
            E: target in list: [-1,0,2,4,6,8] target = 4 output -> 3
               target not in list: nums = [-1,0,2,4,6,8], target = 5
               output -> 4

        M: Binary Search
            nums = [-1,0,2,4,6,8], target = 5
                           l
                             m
                       r
        while l < r
            m = (l + r) // 2
            if target == nums[m]
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
            
        if nums[l] < target:
            return l + 1
        if nums[l] > target:
            return l 
        if nums[r] < target:
            return r + 1
        if nums[r] > target:
            return r 
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return l
