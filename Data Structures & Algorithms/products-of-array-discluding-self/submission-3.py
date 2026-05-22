class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        U: create array where output[i] is prod of all numbers except nums[i]:
            I: int list
            O: int list
            C: 2 <= nums.lenght <= 1000
            E: [-1,0,1,2,3] -> [0,-6,0,0,0]
               [2,3] -> [3,2]
               [1,1,1,1] -> [1,1,1,1] 
        M: prefix and postfix products
        [-1,0,1,2,3] -> [0,-6,0,0,0]
        before -> [1,-1,0,0,0]
        after ->  [0,6,6,3,1]
        final ->  [0,-6,0,0,0]
        P:
        initialize prefix and postfix with 1
        create res list
        loop through nums:
            append prefix to res
            prefix = prefix * num
        loop through nums from back:
            res[i] *= postfix
            postfix *= nums[i]
        return res'''
        
        prefix, postfix = 1, 1
        res = []

        for num in nums:
            res.append(prefix)
            prefix *= num

        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

'''
        R:
        E:
        
        '''