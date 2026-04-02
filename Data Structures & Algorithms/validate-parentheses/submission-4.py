class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        parentheses = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif char in parentheses:  # closing brackets
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False  # invalid character

        return len(stack) == 0
        