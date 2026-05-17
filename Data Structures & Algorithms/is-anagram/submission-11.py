class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        U: check if 2 strings have same characters -> true/false
            I: 2 strings
            O: boolean
            C: both are lowercase only
            E: "car","car" -> true
                "l","j" -> false
                "jar","jam" -> false
                "go", "got" -> false
                "got", "goot" -> false

        M: two hashmaps
        "racecar"  s_count = {r:2, a:2, c:2, e:1}
        "carrace"  t_count = {c:2, a:2, r:2, e:1}

        P: 
        if s and t lens not equal:
            return False

        create two dicts for each string
        populate dicts
        loop through a dict:
            if key not in other dict or key is not equal:
                return false
        return True
        '''
        from collections import Counter
        if len(s) != len(t):
            return False

        s_counter, t_counter = Counter(s), Counter(t)

        for key in s_counter.keys():
            if key not in t_counter or t_counter[key] != s_counter[key]:
                return False
        
        return True






