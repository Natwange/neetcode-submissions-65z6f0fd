class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        tokens = ["1","2","+","3","*","4","-"]
        stack = [9,4]    9 - 4 = 5
        '''
        stack = []

        for item in tokens:
            if item in "+-*/":
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                if item == "+":
                    stack.append(a + b)
                elif item == "-":
                    stack.append(b - a)
                elif item == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(item))
                
        return stack[-1]
