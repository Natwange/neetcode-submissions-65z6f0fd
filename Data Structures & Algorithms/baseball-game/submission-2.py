class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op not in '+DC':
                stack.append(int(op))     
                print(stack[-1])
            else:                         
                if op == '+':               
                    stack.append(stack[-1] + stack[-2])
                elif op == 'D':
                    stack.append(2 * stack[-1]) 
                else:
                    stack.pop()
        return sum(stack)