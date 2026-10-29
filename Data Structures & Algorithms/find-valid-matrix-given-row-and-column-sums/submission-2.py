class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        r_size = len(rowSum)
        c_size = len(colSum)

        matrix = [[0 for _ in range(c_size)] for _ in range(r_size)]

        for r in range(r_size):
            for c in range(c_size):
                matrix[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= matrix[r][c] 
                colSum[c] -= matrix[r][c]

        return matrix