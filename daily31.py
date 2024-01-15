# Find players with zero or one losses
# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.


# Constraints:

# 1 <= matches.length <= 105
# matches[i].length == 2
# 1 <= winneri, loseri <= 105
# winneri != loseri
# All matches[i] are unique.

from typing import List
import itertools

from collections import defaultdict

class Solution:
    def findWinners(self, matches):
        losses = [0] * 100001

        for winner, loser in matches:
            if losses[winner] == 0:
                losses[winner] = -1

            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        zero_loss = [i for i in range(1, 100001) if losses[i] == -1]
        one_loss = [i for i in range(1, 100001) if losses[i] == 1]

        return [zero_loss, one_loss]

# Tests
solution = Solution()
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(solution.findWinners(matches))




