class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        U: looking for the number of days after i where 
        temperature[i] is warmer than at i
            I: int list
            O: int list
            C: 
            E: if len(temperature) < 2 -> [0]

        M: Stack
            [30,38,30,36,35,40,28]  
            [(30,1),(38,1),(40,5)]
            [1,4,1,2,1,0,0]
        P:
            create stack and res [0] * len(temperature)
            loop through temperatures from back:
                while stack and stack[-1] < temperature[i]:
                    stack.pop()
                if stack and stack[-1] > temperature[i]:
                    res[i] == stack[-1][1] - i
                stack.append((temperature[i], i))
            
            return res
        '''
        stack, res = [], [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()

            if stack and stack[-1][0] > temperatures[i]:
                res[i] = stack[-1][1] - i

            stack.append((temperatures[i], i))

        return res


