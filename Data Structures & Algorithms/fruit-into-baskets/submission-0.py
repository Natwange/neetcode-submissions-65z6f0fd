class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        U: return max subarray with two unique chars
            I: int array, i is tree, fruits[i] is fruit type
            O:
            C:
            E:
        
        M: Sliding window
            fruits = [1,2,3,2,2]   window = {2:3,3:1}  res = 4
                        l
                              r
        P
            keep expanding until len(window) > 2
            check if len(window) > 2:
                shrink window
            update res
        '''
        l, res, n = 0, 0, len(fruits)
        window = {}

        for r in range(n):
            window[fruits[r]] = 1 + window.get(fruits[r], 0)

            if len(window) > 2:
                if window[fruits[l]] == 1:
                    del window[fruits[l]]
                else: 
                    window[fruits[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res


