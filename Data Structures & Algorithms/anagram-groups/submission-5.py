class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        U: group anagrams into lists
            I: a list of string strs
            O: a list of lists
            C: all lowercase letters
            E:
                strs = [""] -> [[""]]
                strs = [pot, top] -> [[pot,top]]
                strs = ["x"] -> [["x"]]
                strs = [kit, tip, tim] -> [[kit],[tip],[tim]]
        M:
        ["act","pots","tops","cat","stop","hat"] -> [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        c:1,a:1,t:1 : []

        P:
        if not strs:
            return [[""]]

        make buckets dict
        loop through strs:
            buckets[sorted(str)] = buckets.get(str, [])
        
        res = []
        loop through bucket values:
            append value to res
        
        return res
        '''
        if not strs:
            return [[""]]
            
        buckets = {}
        for word in strs:
            sorted_word = ','.join(sorted(word))
            if sorted_word in buckets:
                buckets[sorted_word].append(word)
            else:
                buckets[sorted_word] = [word]
        
        res = []
        for value in buckets.values():
            res.append(value)
        
        return res
