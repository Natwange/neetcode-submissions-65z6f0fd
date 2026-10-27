import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        U: given n coins, return the number of complete rows of staircase
            I: int n
            O: int
            C: return the number of complete rows
            E: n = 1 -> 1

        M: Binary search
            n = 

        '''
        row = 1
        complete = 0

        while n > 0:
            n = n - row             # n = -2, row = 3, complete = 2
            row += 1
            if n >= 0:
                complete += 1
        return complete
            


