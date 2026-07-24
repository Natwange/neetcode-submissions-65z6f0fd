from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        if t == s: return t

        t_count = Counter(t)
        window = Counter()
        have, need = 0, len(t_count) 
        res, min_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in t and window[s[r]] == t_count[s[r]]:
                have += 1

            while have == need:
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1
                if s[l] in t and window[s[l]] < t_count[s[l]]:
                    have -= 1
                
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = [l, r]
                l += 1

        l, r = res
        return s[l:r + 1] if min_len != float('inf') else ''