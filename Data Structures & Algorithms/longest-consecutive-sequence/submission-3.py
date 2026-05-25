class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        U: look for the longest consetive run +1
            I: int array
            O: int
            C: 
                there must be consecutive plus one run, no gaps
                O(n) solution
            E:
                [1,2,3,3,4,5] -> 4
                [9,1,4,7,3,-1,0,5,8,-1,6] -> 7
        M: set and max vs min
        '''
        if not nums:
            return 0

        mini = min(nums) 
        curr_longest = 0
        final_longest = 0
        nums_set = set(nums)

        while nums_set:
            if mini in nums_set: 
                curr_longest += 1 
                nums_set.remove(mini)
                mini += 1 
                final_longest = max(curr_longest, final_longest)
            else:
                curr_longest = 0
                mini = min(nums_set)  

        return final_longest
                
    
