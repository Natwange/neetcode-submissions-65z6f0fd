class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "jar", t = "jam"
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for char in s:
            countS[char] = 1 + countS.get(char, 0) 
            #countS = {j:1, a:1, r:1}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            #countT = {j:1, a:1, m:1}

        for char in countS:
            if char not in countT:
                return False
            if countS[char] != countT[char]:
                return False
        return True