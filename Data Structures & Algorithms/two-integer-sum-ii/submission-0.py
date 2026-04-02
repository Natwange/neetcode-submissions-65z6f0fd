class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Understand: return indices(1-indexed) of two numbers that add 
        to a target
            I: int array sorted in non-desc order
            O: list of two indices (1-indexed)
            C: dupes allowed, index1 < index2, index1 != index2, no empty list
            E: even and odd lists

        Method: Binary search

        Plan:
        midpoint = (0 + len(nums) - 1) // 2
        if midpoint > target:
            l, r = 0, midpoint - 1

        while r > l:
            num[r] + num[]



        Implement:
        '''
        l, r = 0, len(numbers) - 1
        mid = (l + r) // 2

        while r > l:
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            else:
                if numbers[r] + numbers[l] > target:
                    r -= 1
                else:
                    l += 1


        '''
        Review:

        Evaluate:
        '''
        