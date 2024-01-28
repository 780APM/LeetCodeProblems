# K inverse pairs array
# Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.
# We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.
# Since the answer may be very large, the answer should be modulo 109 + 7.

# Example 1:
# Input: n = 3, k = 0
# Output: 1
# Explanation:
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7 #  10^9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)] # dp[i][j] = number of arrays that have j inverse pairs with length i
        dp[0][0] = 1 # base case

        for i in range(1, n + 1): # iterate through the length of the array
            dp[i][0] = 1 
            for j in range(1, k + 1): # iterate through the number of inverse pairs
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod # dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - i]
                if j - i >= 0: # if j - i is greater than or equal to 0
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + mod) % mod # dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - i]

        return dp[n][k]