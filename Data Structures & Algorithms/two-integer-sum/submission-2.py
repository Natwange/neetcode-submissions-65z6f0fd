class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        U:
        Input: nums int list
        Output: 2 ints nums[i] + nums[j] == target

        M: Hash map

        P:
        create a dict
        loop through nums
            if num in dict:
                return [dict[num], num index]
            else:
                map target-num: index of num
        I:
        '''
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[target - nums[i]] = i 
        '''
        R:

        E:
        '''