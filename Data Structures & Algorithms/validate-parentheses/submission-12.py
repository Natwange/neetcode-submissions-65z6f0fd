class Solution:
    def isValid(self, s: str) -> bool:
        #"([{}])"
        #length of input must be even
        if len(s) % 2 != 0:
            return False
        
        #close_to_open dict
        close_to_open = {"]":"[", "}":"{", ")":"("}

        #stack for opening parathesis
        stack = []

        #"([{}])"
        #loop through string:
        for char in s:
            #if open add to stack
            if char in close_to_open.values():
                stack.append(char)   # stack = [ {[( ]
            elif stack and close_to_open[char] != stack[-1]:
                return False
            elif stack and close_to_open[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack


     
     
    






     