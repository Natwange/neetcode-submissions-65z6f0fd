from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return "" 

        t_counter = Counter(t)
        window = {}
        res = [-1, -1]
        res_len = float('inf')
        l = 0
        have, need = 0, len(t_counter)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in t_counter and window[s[r]] == t_counter[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
                    have -= 1

                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""