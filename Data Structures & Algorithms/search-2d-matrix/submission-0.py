class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        U: search for target in a 2D matrix
            I: 2D matrix (list of lists)
            O: boolean
            C: row sort in ascending order
               row starting value is greater than prev role end value
               solve in O(log(m * n))
            E: m=1, n=1, false if target is absent, otherwise true

        M: Binary search

        P:
        '''

        l, r = 0, len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue

            while l <= r:
                mid = (l + r) // 2

                if matrix[i][mid] == target:
                    return True

                elif matrix[i][mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1
        
        return False
