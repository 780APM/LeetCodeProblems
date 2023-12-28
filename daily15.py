# run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) 
# with the concatenation of the character and the number marking the count of the characters (length of the run).
# For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". 
# Thus the compressed string becomes "a2bc3".

# Example 1:
# Input: s = "aaabcccd", k = 2 
# Output: 4 
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6.
# Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5,
# for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d.
# Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

# constraints:
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.

class Solution: 
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def f(start, pre, last_count, left):
            if left < 0:
                return float("inf") 
            if start >= len(s):
                return 0
            if s[start]==pre:
                incr = 1 if last_count in (1,9,99) else 0 
                return incr + f(start+1, pre, last_count+1, left) 
            else:
                keep = 1  + f(start+1, s[start], 1, left) 
                delete = f(start+1, pre, last_count, left-1) 
                return min(keep, delete)
        return f(0,"", 0,k)
    
# Test Program
s = "aaabcccd"
k = 2
print(Solution().getLengthOfOptimalCompression(s, k))  # Expected output: 4