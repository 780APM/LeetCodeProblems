# Constraints:

# 1 <= arr.length <= 500
# 0 <= arr[i] <= 109
# 1 <= k <= arr.length

from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            curMax = 0
            for j in range(1, k + 1):
                if i - j + 1 >= 0:
                    curMax = max(curMax, arr[i - j + 1])
                    dp[i] = max(dp[i], dp[i - j] + curMax * j)
        return dp[n - 1]