# maximum profit by job scheduling
# we have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# you're given the startTime, endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range`
# if you choose a job that ends at time X you will be able to start another job that starts at time X

# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: the subset chosen is the first and fourth job.
# time: O(n^2)

import bisect
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the startTime, endTime, and profit into a list of jobs and sort them by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])

        # Initialize the dynamic programming list with a dummy job
        dp = [[0, 0]]

        # Iterate over the sorted list of jobs
        for s, e, p in jobs:
            # Use binary search to find the job with the largest end time that is less than or equal to the start time of the current job
            i = bisect.bisect(dp, [s + 1]) - 1

            # If scheduling the current job after the job at index i would result in a higher total profit, append the current job and the new total profit to the dp list
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])

        # Return the maximum profit, which is the profit of the last job in the dp list
        return dp[-1][1]
            
# test cases
sol = Solution() # create an instance of the Solution class
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
print(sol.jobScheduling(startTime, endTime, profit)) # call the method on the instance

sol = Solution() # create an instance of the Solution class
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(sol.jobScheduling(startTime, endTime, profit)) # call the method on the instance


