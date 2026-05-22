class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False

        s_counter, t_counter = Counter(s), Counter(t)

        #for key in s_counter.keys():
          #  if s_counter[key] != t_counter.get(key, 0):
            #    return False

        return s_counter == t_counter






