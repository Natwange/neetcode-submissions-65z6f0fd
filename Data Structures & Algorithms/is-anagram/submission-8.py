class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)
        #return Counter(s) == Counter(t)
        
        
        if len(s) != len(t):
            return False
            
        s_counter, t_counter = Counter(s), Counter(t)
        
        for char, count in s_counter.items():
            if char not in t_counter or count != t_counter[char]:
                return False
                
        return True
        





       
    