# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

#Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): # If the lengths are not equal, they are not anagrams
            return False
        count = [0] * 26 # Create a list of 26 zeroes 
        for i in range(len(s)): # Iterate through the strings
            count[ord(s[i]) - ord('a')] += 1 # Increment the count of the character in the list
            count[ord(t[i]) - ord('a')] -= 1 # Decrement the count of the character in the list 
        for c in count: # Iterate through the list
            if c != 0: # If any of the counts are not zero, they are not anagrams
                return False # Return False if the counts are not zero
        return True # If all the counts are zero, they are anagrams

# Test the function
s = "anagram"
t = "nagaram"
sol = Solution()
result = sol.isAnagram(s, t)
print(result)