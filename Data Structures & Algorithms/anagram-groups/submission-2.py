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

        letter_list = defaultdict(list)
        res = []

        for word in strs:
            letter_list[''.join(sorted(word))].append(word)
        
        for ana_list in letter_list.values():
            res.append(ana_list)

        return res






        '''
        Review:

        Evaluate:
        '''