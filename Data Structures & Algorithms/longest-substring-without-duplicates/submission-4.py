class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Plan:
        create curr_len and max_len
        create pointer 
        loop through string
            if r in prev substring:
                move l while r in prev substring
            calculate curr_len and max_len

        Implement:
        "zxyzxyyy"
        '''
        curr_len, max_len = 0, 0
        l = 0

        for r in range(len(s)):
            #if s[r] in s[l:r]:
            while s[r] in s[l:r] and l < r:
                l += 1
            curr_len = r - l + 1
            max_len = max(curr_len, max_len)

        return max_len

        '''
        Review:

        Evaluate:
        '''