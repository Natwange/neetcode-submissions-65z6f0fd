class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        U: return 2 positions with numbers that add up to target
            I: int and int array
            O: two ints
            C: i !=J
               each target has a solution
               smaller index first in output
            E:  [3,4,5,10], 15 -> [2,3]
                [3,4,5,6], 7 -> [0,1]
                [3,4,5,6], 9 -> [1,2]
                [3,4,6,8,10,11], 14  -> [1, 4]
                {11:0, 10:1, 8:2,}

        Method: hash map index:target-num[index]
        nums = [3,4,5,6], target = 7

        Plan:
        create dict
        loop though nums:
            if num in dict:
                return [dict[num], index of num]
            dict[target - num] = index
        '''

        map = {}

        for index, num in enumerate(nums):
            if num in map:
                return [map[num], index]

            map[target - num] = index
        
        




