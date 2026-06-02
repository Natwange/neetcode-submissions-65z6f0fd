class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # U: returning a target number in a list
        # M: Binary Search
        # P:
        low, high = 0, len(nums) - 1
        
        while high >= low:
            mid = low + (high - low) // 2

            if nums[mid] == target:
              return  mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
