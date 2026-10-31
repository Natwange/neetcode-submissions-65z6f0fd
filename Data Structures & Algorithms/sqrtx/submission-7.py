class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        U: return square root of integer x rounded down to int
            I: int x
            O: int 
            C: rounded down to nearest int
            E: x = 13 -> 3

        M: Binary Search
            l = 0, r = x//2,
            x = 24, l = 3, r = 5, mid = 4   ans = min(ans,mid) = 2
            [0,1,2,3,4,5,6,7,8,9,10,11,12]   [0,1,2,3,4,5,6,7,8]
                   l                          l
                     m                              m
                       r                                    r
            last value of m?
        
        '''
        if x == 0:
            return 0

        if x < 4:
            return 1

        #max_root = x // 2
        l, r = 0, x
        res = 0

        while l <= r:
            m = (l + r) // 2

            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
                res = m
            else:
                r = m - 1

        return res