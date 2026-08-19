class Solution:
    def mySqrt(self, x: int) -> int:
        '''
                9
              /   \
             3     3
            l=1    r=9
            m=9 // 2 = 4  4*4 = 16
            l=1   r=3  m=2     2*2=4
            l=3  r=3  m=3    3*3 = 9

          l = 1, r = 13, m = 7, 7*7=49
          l=1, r=8, m=3, 3*3=9
          l=4, r=8, m=6, 6*6 = 24
          l=4, r=5, m=4, 16
          l=5, r=5, m=5, 25
          l=5, r=4,
          13
        '''
        if x < 2:
            return x
        
        l, r = 1, x

        while l <= r:
            mid = (l + r) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

        