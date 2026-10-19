class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        U: perform operations in operations to find the list of integers to sum at the end.
        P:
        stack = []

        loop through operations:
            if op.isdigit():
                stack.append(op)
            else:
                if op == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif op == 'D':
                    c = stack.pop() * 2
                    stack.append(c / 2)
                    stack.append(c)
                else:
                    stack.pop()
        '''
        stack = []

        for op in operations:
            if op not in '+DC':
                stack.append(int(op))     # ops=["5","-2","4","C","D","9","+","+"] ans = 27
                print(stack[-1])
            else:                         # stack = [5,-2,-4,9,]
                if op == '+':               
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b)
                    stack.append(a)
                    stack.append(a + b)
                elif op == 'D':
                    c = stack.pop()
                    stack.append(c) 
                    stack.append(c * 2)
                else:
                    stack.pop()
        return sum(stack)