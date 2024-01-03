# number of Laser Beams in a bank
# Anti-theft secutiy evices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.
# There is one laser beam between any two security devices if both conditions are met:
# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.

# example 
# bank = ["011001","000000","010100","001000"]
# output = 8 


# constrains 
# m == bank.length
# n == bank[i].length
# 1 <= m, n <= 200
# bank[i][j] is either '0' or '1'.

# solution
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev_count = 0
        for row in bank:
            if '1' in row:
                count = row.count('1')
                if prev_count > 0:
                    result += prev_count * count
                prev_count = count
        return result

# test cases
sol = Solution() # create an instance of the Solution class
bank = ["011001","000000","010100","001000"]
print(sol.numberOfBeams(bank)) # call the method on the instance