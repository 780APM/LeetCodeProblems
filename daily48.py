# Divide Array into arrays with max difference 
# given an intiger array 'nums' of size 'n' and a positive integer 'k'
# Divide the array into one or more arrays of size 3 satisfying the following conditions:
# each element of the array is in exactly one array
# the difference between the maximum and minimum element of each array is less than or equal to k
# Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return any of them.

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Check if the length of nums is a multiple of 3
        if len(nums) % 3 != 0 or len(nums) < 1 or len(nums) > 105:
            return []
        
        # Check if k is between 1 and 105
        if k < 1 or k > 105:
            return []
        
        # Check if each element in nums is between 1 and 105
        for num in nums:
            if num < 1 or num > 105:
                return []
        
        # Sort the array
        nums.sort()
        
        result = []
        for i in range(0, len(nums), 3):
            # Check if the difference between the maximum and minimum elements in the subarray is not greater than k
            if nums[i+2] - nums[i] > k:
                return []
            result.append(nums[i:i+3])
        
        return result
    

class Solution:
    def divideArray(self, nums, k):
        size = len(nums)
        if size % 3 != 0:
            return []

        nums.sort()

        result = []
        group_index = 0
        for i in range(0, size, 3):
            if i + 2 < size and nums[i + 2] - nums[i] <= k:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
                group_index += 1
            else:
                return []
        return result

