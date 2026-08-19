# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

'''
U: guess the correct number through a predefined api guess
    I: int n
    O: int
    C: answer between 1 and n
    E: when n == pick
       
    M: Binary Search

    n = 5 
    lower = 1, upper = 5, mid = 3    pick = 5
    mid = 3 -> guess(3) == 1
    lower = 4, upper = 5, mid = 4
    mid = 4 -> guess(4) == 1
    lower = 5, upper = 5, mid = 5
    mid = 5 -> guess(5) == 0, return mid
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 1, n

        while lower <= upper:
            mid = (lower + upper) // 2

            if guess(mid) == 0:
                return mid

            elif guess(mid) == -1:
                upper = mid - 1

            elif guess(mid) == 1:
                lower = mid + 1