class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 0, num // 2

        while l <= r:
            mid = (l + r) // 2
            prod = mid * mid 

            if prod == num:
                return True
            if prod > num:
                r = mid - 1
            elif prod < num:
                l = mid + 1

        return False