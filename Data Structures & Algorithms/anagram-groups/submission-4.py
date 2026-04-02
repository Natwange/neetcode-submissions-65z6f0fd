class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Understand: Group anagrams together in seperate lists
            I: list of strings
            O: list of lists of strings
            C: 1 <= strs.length <= 1000 and 0 <= strs[i].length <= 100
            E:
                no anagrams: ['act','x','top'] -> [['act'],['x'],['top']]
                same words: ['cat','cat','cat'] -> [['cat','cat','cat']]
                single: ['x'] -> [['x']]
                empty: [""] -> [[""]]  
                more empty: ["",""] -> [["",""]]

        Method: HashMap grouping

        Plan:
            1. dictionary letter_list = {}
            2. loop through strs:
                    add letter[str.sort].append[str] 
        Implement:
        '''

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(word)

        return list(res.values())





        '''
        Review:

        Evaluate:
        Time: O(n*klogk)
        Space: O(n · k)
        '''