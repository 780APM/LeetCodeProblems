class Solution:
    def imageSmoother(self, M):
        rows, cols = len(M), len(M[0])
        new_grid = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                sum, count = M[i][j], 1
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if (di, dj) != (0, 0):  # Exclude the current cell
                            ni, nj = i + di, j + dj
                            if 0 <= ni < rows and 0 <= nj < cols:
                                sum += M[ni][nj]
                                count += 1
                new_grid[i][j] = sum // count
        return new_grid
    
# test case
s = Solution()
M = [[1,1,1],[1,0,1],[1,1,1]]
print(s.imageSmoother(M)) # [[0,0,0],[0,0,0],[0,0,0]]