# maximum score after splitting a string

# given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
# the score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

# example 1:
# input: s = "011101"
# output: 5
# explanation:
# all possible ways of splitting s into two non-empty substrings are:
# left: "0" and right: "11101", score = 1 + 4 = 5
# left: "01" and right: "1101", score = 1 + 3 = 4
# left: "011" and right: "101", score = 1 + 2 = 3
# left: "0111" and right: "01", score = 1 + 1 = 2
# left: "01110" and right: "1", score = 2 + 1 = 3

# constraints:  2 <= s.length <= 500 
# the string s consists of characters '0' and '1' only.

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_score = 0
        for i in range(1, len(s)): # i is the index of the first character of the right substring
            left = s[:i] # left substring
            right = s[i:] # right substring
            score = left.count('0') + right.count('1') # score of this split
            max_score = max(max_score, score) # update max_score
        return max_score # return max_score after all splits
    
    # testcase
    s = "011101"
    print(maxScore(s)) # 5
    s = "00111"
    print(maxScore(s)) # 5
    s = "1111"
    print(maxScore(s)) # 3
    s = "00"
    print(maxScore(s)) # 1

# time complexity: O(n^2)
# space complexity: O(n)
    
    