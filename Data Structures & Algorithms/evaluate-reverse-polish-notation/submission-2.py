class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            elif len(stack) > 1: 
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "/":
                    res = int(a / b)
                else: 
                    res = a * b

                stack.append(res)
            
        return stack[-1]