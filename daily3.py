# Special Positions in a Binary Matrix, Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # create two lists to store the number of 1s in each row and each column
        rowCount = [0] * len(mat)
        colCount = [0] * len(mat[0])
        # loop through the matrix and increment the count of 1s
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1
        # create a counter to store the number of special positions
        counter = 0
        # loop through the matrix again
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # if the element is 1, check if the row and column have exactly one 1
                if mat[i][j] == 1 and rowCount[i] == 1 and colCount[j] == 1:
                    # if they do, increment the counter
                    counter += 1
        return counter
    
# test case
s = Solution()
print(s.numSpecial([[1,0,0],[0,0,1],[1,0,0]]))

