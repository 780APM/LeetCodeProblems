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
    def minOperations(self, nums: List[int]) -> int:
        # Create a Counter object from nums. This will count the occurrences of each number in nums.
        mp = Counter(nums)
        
        # Initialize a variable count to 0. This will keep track of the total number of operations.
        count = 0
        
        # Iterate over the values in mp (which are the counts of each number in nums).
        for t in mp.values():
            # If t is 1, return -1. This means there's a number in nums that only appears once, so it's impossible to empty the array.
            if t == 1:
                return -1
            
            # Add t // 3 to count. This is the number of times you can perform the operation on this number.
            count += t // 3
            
            # If t has a remainder when divided by 3 (t % 3), add 1 to count. This means one more operation is needed for this number.
            if t % 3:
                count += 1
                
        # After the loop, return count. This is the minimum number of operations needed to empty the array.
        return count

# test cases
sol = Solution() # create an instance of the Solution class
nums = [2,3,3,2,2,4,2,3,4]
print(sol.minOperations(nums)) # call the method on the instance

nums = [2,1,2,2,3,3]
print(sol.minOperations(nums))
