# minimum number of operations to make array empty
# you are given a 0-indexed array nums consisting of positive integers
# there are two types of operations you can perform on nums

# example 1: 
# nums = [1,2,3,4,5,6]
# output = 9
# explanation:

# constraints 
# 2 <= nums.length <= 105
# 1 <= nums[i] <= 10^6

# solution

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int: # nums is a list of integers
        from collections import Counter
        mp = Counter(nums)
        
        count = 0 # number of operations
        for t in mp.values(): # t is the value of the key
            if t == 1: # if there is only one value
                return -1 # return -1 
            count += t // 3 # count is the number of operations
            if t % 3: # if there is a remainder
                count += 1 # add 1 to the count
                
        return count

# test cases
sol = Solution() # create an instance of the Solution class
nums = [2,3,3,2,2,4,2,3,4]
print(sol.minOperations(nums)) # call the method on the instance

nums = [2,1,2,2,3,3]
print(sol.minOperations(nums))