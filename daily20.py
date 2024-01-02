# Convery an array into a 2D array with conditions
# you are given an interger array nums, you need to create a 2D array from nums satisfying the following conditions:
# 1. The 2 array should contain only the elements of the array nums
# 2. Each row of the 2D array contains disctinct integers
# 3. The number of rows in the 2D array should be minimal 

from typing import List # import the List class from the typing module

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]: # nums is a list of integers
        result = [] # initialize the result
        for num in nums: # for each number in nums
            for row in result: # for each row in result 
                if num not in row: # if the number is not in the row 
                    row.append(num) # append the number to the row
                    break
            else: # if the number is in the row
                result.append([num]) # append the number to a new row
        return result # return the result
    
    # test cases
sol = Solution() # create an instance of the Solution class
nums = [1,2,3,3,3,3,4,5] # list of integers
print(sol.findMatrix(nums)) # call the method on the instance
nums = [1,1,1,1,1,1,1,1] # list of integers
print(sol.findMatrix(nums)) # call the method on the instance
