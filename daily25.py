# arithmatic slices - 446

# given a integer array nums, return the number of arithmetic subsequences of nums
# a sequence of numbers is called arithmetic if it consists of at least three elements 
# and if the difference between any two consecutive elements is the same

# constraints 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1

from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int: 
        count = 0 # number of arithmetic subsequences
        dp = [defaultdict(int) for _ in nums] # dp[i][diff] = number of arithmetic subsequences ending at index i with difference diff
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j] # difference between nums[i] and nums[j]
                dp[i][diff] += 1 # add 1 to dp[i][diff] because nums[i] and nums[j] form an arithmetic subsequence
                if diff in dp[j]: # if nums[j] can be added to an existing arithmetic subsequence ending at index j with difference diff
                    dp[i][diff] += dp[j][diff] # add the number of arithmetic subsequences ending at index j with difference diff to dp[i][diff]
                    count += dp[j][diff] # add the number of arithmetic subsequences ending at index j with difference diff to count 
                    
        return count

# test cases
nums = [2, 4, 6, 8, 10]
# create an instance of the Solution class
sol = Solution()
# call the method on the instance of the class, passing nums as an argument
print(sol.numberOfArithmeticSlices(nums))  # Output: 7

nums = [7, 7, 7, 7, 7]
print(sol.numberOfArithmeticSlices(nums))  # Output: 16