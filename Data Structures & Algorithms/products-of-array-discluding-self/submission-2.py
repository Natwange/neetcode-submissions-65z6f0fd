class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        U: return  array of product of numbers except self
            I: int array
            O: int array
            C: 
                2 <= nums.length <= 1000
                -20 <= nums[i] <= 20
            E:
                [2,3] -> [3, 2]
                [1, 2, 0, 4] -> [0, 0, 8, 0]

        M: Prefix/postfix array traversal
        P:
            prefix,postfix = 1
            make res = []

            prefix loop through nums:
                append to res =  prefix * num
                prefix = prefix * num
            
            postfix/final loop through nums start from back:
                res[i] = post * num
                postfix = postfix * num

            return res 
        I:
        '''
        prefix, postfix = 1, 1
        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]   

        return res







        '''
        R:
        E:
        '''
