class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:                  
                top = stack[-1]                       
                res[top] = i - top
                stack.pop()
            stack.append(i)
        return res



