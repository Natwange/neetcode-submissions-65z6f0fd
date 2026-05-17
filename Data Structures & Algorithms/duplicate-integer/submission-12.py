class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        U: checking for dupes in array
            I: an int list
            O: boolean
            C: 
            E: [] -> false
               [1] -> false
               [1, 2, 2, 3] -> true
        P:
        create a seen dict
        Loop through nums
            if the curr num is in seen:
                return True
            add num to seen
        return False
        """
        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = 1

        return False