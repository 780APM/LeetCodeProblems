# Unique Number of Occurrences

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for n in arr:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        return len(d) == len(set(d.values()))
    
# Tests
solution = Solution()
arr = [1,2,2,1,1,3]
print(solution.uniqueOccurrences(arr))
    
        