# Two strings are considered close if you can attain one from the other using the following operations:
# Operation 1: Swap any two existing characters. For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character. For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): # if word1 and word2 are not the same length, return False
            return False

        counter1 = Counter(word1)
        counter2 = Counter(word2)

        # Check if the two words have the same unique characters
        if set(counter1.keys()) != set(counter2.keys()):
            return False

        # Check if the two words have the same frequency of characters
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False

        return True

# test cases
        
# create an instance of the Solution class
sol = Solution()
# call the method on the instance of the class, passing nums as an argument
print(sol.closeStrings("abc", "bca"))  # Output: True
print(sol.closeStrings("a", "aa"))  # Output: False