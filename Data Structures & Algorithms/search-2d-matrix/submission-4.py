class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix[0])*len(matrix)-1

        s = len(matrix[0])

        while l <= r:
            m = (l+r)//2
            i1 = m // s
            i2 = m % s


            if matrix[i1][i2] > target:
                r = m - 1
            elif matrix[i1][i2] < target:
                l = m + 1
            else:
                return True
        
        return False