class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        U: returning a list of ints where num[i] is prod of 
        all other numbers except num[i]
            I: int list
            O: int list
            C: 
            E: [-1,0,1,2,3] -> [0,-6,0,0,0]
                [1,5] -> [5,1]
        
        M: arrays
            [1,2,4,6]
            before = [1,1,2,8]
            after = [48,24,6,1]
            res = [48,24,12,8]
        
        P:
        [1,0,1,2,3]  res=[1,1,0,0,0] prefix = 0, post = 6
    
        '''
        res = []
        prefix, post = 1, 1

        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res  
        