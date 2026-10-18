class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(a):   # if stack here redundant?  
                    stack.pop()
                    #stack.append(a)
                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                    a = 0
                else:                             # a = -5
                    a = 0                         # [10,2,-5]
            if a != 0:                            # stack = [10]
                stack.append(a)
        return stack


