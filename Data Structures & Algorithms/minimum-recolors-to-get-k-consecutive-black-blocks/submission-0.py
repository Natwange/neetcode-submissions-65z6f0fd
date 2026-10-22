class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        U: return the min num of operations to get k consecutive black blocks
            I: str
            O: int
            C: consecutive and len k
            E: 'W' -> 1 'B'
                'wwww' k=4  

        M: Sliding window
            blocks = "WBBWWBBWBW", k = 7, w_count = 3, min_op = 3
                         l
                               r
            if r - l + 1 == k:
                update min_op
        '''
        n = len(blocks)
        l, w_count = 0, 0
        min_op = float('inf')

        for r in range(n):
            if blocks[r] == 'W':
                w_count += 1
            if (r - l + 1) == k:
                min_op = min(min_op, w_count)  
                if blocks[l] == "W":
                    w_count -= 1
                l += 1 
        
        return min_op
        '''blocks = "WBBWWBBWBW", k = 7, w_count = 3, min_op = 3
                        l 
                              r
        
        '''




