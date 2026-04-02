class Solution:
    def isValid(self, s: str) -> bool:
        '''
        U:
            I: string
            O: boolean
            C: 1 <= s.length <= 1000
            E: 
                1. uneven number of parenthesis -> False
                2. ")(" -> False, opening first

        M: Stack, dictionary
        P:
            if len(s) uneven return false
            create stack
            create close -> open map
            loop through s:
                if open:
                    add to stack
                elif close:
                    with close->open map, check if open == stack[-1]:
                        if yes, stack.pop(open)
                        else return False
            return True

        I:
        '''
        if len(s) % 2 != 0:
            return False

        stack = []
        close_to_open = {")":"(", "]":"[", "}":"{"}

        if s[0] in close_to_open.keys():
            return False

        for char in s:
            if char in close_to_open.values():
                stack.append(char)
            elif stack and close_to_open[char] != stack[-1]:
                return False
            elif stack and close_to_open[char] == stack[-1]:
                stack.pop()
        return not stack    
        
        '''

        R:

        E:
        '''

        