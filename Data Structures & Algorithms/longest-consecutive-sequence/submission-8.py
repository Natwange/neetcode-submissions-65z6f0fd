class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            count = 0
            if num - 1 not in nums_set:
                while num in nums_set:
                    num += 1
                    count += 1
                longest = max(longest, count)
        return longest