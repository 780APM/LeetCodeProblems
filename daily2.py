# maximum product of two elements in an array 

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

# create a test case
s = Solution()
nums = [3,4,5,2]
print(s.maxProduct(nums))