# Difference Between Ones and Zeros in Row and Column

class Solution(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])
        rowSum = [0]*m
        colSum = [0]*n
        diff = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                rowSum[i] += 2*grid[i][j] - 1
                colSum[j] += 2*grid[i][j] - 1

        for i in range(m):
            for j in range(n):
                diff[i][j] = rowSum[i] + colSum[j]

        return diff