class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        U: returning true if theres duplicate, otherwise false
            I: array
            O: true/false (boolean)

        P: 
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
        I: 
        '''
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False