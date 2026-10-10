class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        strs = ['Hello', 'World']
        encoded = '5#Hello5#World'
        '''
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            word_len = ''          
            while s[i] != '#':     
                word_len += s[i]
                i += 1
            res.append(s[i+1:i+1+int(word_len)])
            i = i + 1 + int(word_len)
        return res


