class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                count = 0
                while num in nums_set:
                    num += 1
                    count += 1
                longest = max(longest, count)
        return longest