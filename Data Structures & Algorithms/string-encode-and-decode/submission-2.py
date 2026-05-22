class Solution:
    '''
    U: input list converted to sing string(encode), output
    is converted  back to original input lis
        I: list of string
        O: list of string
        C:
        E:
            [""] -> [""] -> [""]
            ["queen"] -> ["queen"]
            ["queen", "princess"] -> ["queen#princess"] -> ["queen", "princess"]
        
        M: 
        ["3#Hello#2","#2World3"] -> [""] -> ["Hello","World"]

    
    '''

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res




