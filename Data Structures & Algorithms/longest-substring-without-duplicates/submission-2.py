class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Understand:
        Returning the length(an int) of longest substring 
        without repeating characters.
        Input: string
        Outout: int
        Constraints: 0 <= s.length <= 1000
        Edge cases:
        1. no repeats: "xxxx" => 1
        2. whole string has no repeats: "xyz" => 3
        3. empty: "" => 0 
        4. repeat happens immediatey: "abba" => 2

        Method:
        Sliding window technique and dictionary
        "abba" => 2
           ||
        {a:1, b:1} curr_len = 2
        {b:1, a:1} curr_len = 2
        return max_len

        "pwwkew" => 3
           ||
        {p:1, w:1} curr_len = 2
        {w:1, k:1, e:1} curr_len = 3
        return max_len

        Plan:
        l, r, max_len = 0
        dict = {}

        loop through s:
            if s[r] not in dict:
                add it
            else if s[r] in dict:
                l = r
                dict = {}
                dict add s[r]
            r += 1
            curr_len = len(dict)
            max_len = max(curr_len, max_len)

        Implement:
        """
        '''l, r, max_len = 0, 0, 0
        dicti = {}

        while r < len(s): 
            if s[r] not in dicti:
                dicti[s[r]] = 1
                r += 1
            elif s[r] in dicti:
                l = r
                dicti = {}
                dicti[s[r]] = 1
                r = l
            curr_len = len(dicti)
            max_len = max(curr_len, max_len)
        
        return max_len'''

        l = 0
        counter = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in counter:
                counter.remove(s[l])
                l += 1
            counter.add(s[r])
            max_len = max(max_len, r- l+1)

        return max_len



        










        """
        Review:

        Evaluate:
        """

        
