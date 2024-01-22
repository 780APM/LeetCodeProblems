# set mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, 
# one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# constraints:
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104

from typing import List # import List for type hinting

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        duplicate = sum(nums) - sum(set(nums)) # find the duplicate
        missing = sum(range(1, n + 1)) - sum(set(nums)) # find the missing number
        return [duplicate, missing]
    
# Tests
solution = Solution()
nums = [1,2,2,4]
print(solution.findErrorNums(nums))

nums = [2,2]
print(solution.findErrorNums(nums))