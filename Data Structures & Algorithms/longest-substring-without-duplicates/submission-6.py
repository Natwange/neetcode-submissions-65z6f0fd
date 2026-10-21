class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        U: return LEN of longest substring without dupes
            I: string s
            O: int
            C: no dupes
            E: "xxxx" -> 1, 'x' -> 1, "xyz" -> 3

        M: Sliding window + set
            s = "zxyzxyz"       set=xyz, res=3
                     l              
                       r
        P:
        s_set = set()
        l, n = 0, len(s)
        res = 0

        for r in range(n):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            res = max(res, r-l+1)

        return res
        '''
        s_set = set()
        l, n = 0, len(s)
        res = 0

        for r in range(n):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            res = max(res, r-l+1)

        return res




