# You are given a string s of even length. 
# Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels 
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

#Constraints:
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.



import unittest

class Solution:
    def halvesAreAlike(self, s: str) -> bool: # function halvesAreAlike with string s as input argument and returns a boolean
        vowels = "aeiouAEIOU" # string of vowels
        a = s[:len(s)//2] # string a is the first half of string s
        b = s[len(s)//2:] # string b is the second half of string s
        a_count = 0 # initialize a_count to 0
        b_count = 0 # initialize b_count to 0
        for i in a: # for each character i in string a
            if i in vowels: # if i is in vowels
                a_count += 1 # increment a_count by 1
        for i in b: # for each character i in string b
            if i in vowels: # if i is in vowels
                b_count += 1 # increment b_count by 1
        return a_count == b_count # return True if a_count is equal to b_count, otherwise return False
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_halvesAreAlike(self):
        # Test case 1
        s = "book"
        expected = True
        self.assertEqual(self.solution.halvesAreAlike(s), expected, "Failed on Test Case 1")

        # Test case 2
        s = "textbook"
        expected = False
        self.assertEqual(self.solution.halvesAreAlike(s), expected, "Failed on Test Case 2")

        # Test case 3
        s = "MerryChristmas"
        expected = False
        self.assertEqual(self.solution.halvesAreAlike(s), expected, "Failed on Test Case 3")

        # Test case 4
        s = "AbCdEfGh"
        expected = True
        self.assertEqual(self.solution.halvesAreAlike(s), expected, "Failed on Test Case 4")

if __name__ == '__main__':
    unittest.main()

# testcase
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
