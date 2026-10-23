class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        U: return true is s2 has a permutation of s1, otherwise return false
            I: two strings
            O: boolean
            C: len(s1) < len(s2)
            E: s1='abcd' s2='abc' -> False
               s1='abc' s2='abcd'-> True
               s1='abc' s2='abc' -> True
        
        M: Sliding Window + Hash map
            s1 = "abc", s2 = "lecabee"  s1_map = {a:1,b:1,c:1}  s2_map = {c:1,a:1,b:1}
        P:

        s2_map must contain len(s1) chars at a time
        compare s2_map and s1_map
        if the maps are equal, immediately return True
        '''
        if len(s1) > len(s2): return False
        if s1 == s2: return True
        s1_map = Counter(s1)
        s1_num_chars = sum(s1_map.values())
        s2_map = {}
        s2_num_chars = 0
        l, n = 0, len(s2)
        
        '''s1 = "adc", s2 = "dcda"  s1_map = {a:1,d:1,c:1}  s2_map = {d:1,c:1,a:1}
                              l
                                r              '''

        for r in range(n):
            s2_map[s2[r]] = 1 + s2_map.get(s2[r], 0)
            s2_num_chars += 1
            print(s2_map)
            if s2_num_chars == s1_num_chars:
                if s2_map == s1_map:
                    return True
                if s2_map[s2[l]] == 1:
                    del s2_map[s2[l]]
                elif s2_map[s2[l]] > 1:
                    s2_map[s2[l]] -= 1
                l += 1
                s2_num_chars -= 1
        return False







