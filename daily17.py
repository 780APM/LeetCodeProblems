# Redistriute character to make all strings equal

from typing import List
from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words) # number of words
        if n == 1: # if there is only one word, it is always true
            return True 
        count = Counter() # count the number of each character
        for word in words: 
            for c in word:
                count[c] += 1 
        for c in count:
            if count[c] % n != 0: # if the number of a character is not divisible by the number of words, it is false
                return False
        return True
    
# test case 
sol = Solution()  # create an instance of the Solution class
words = ["abc","aabc","bc"]  # true
print(sol.makeEqual(words))  # call the method on the instance
words = ["ab","a"]  # false
print(sol.makeEqual(words))  # call the method on the instance
