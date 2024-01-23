# maximum length of a concatenated string with unique characters

# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

# constraints and notes

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.


from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Create a variable to store the maximum length of a concatenated string with unique characters
        max_length = 0
        
        # Create a function to check if a string has unique characters
        def has_unique_characters(string):
            # Create a dictionary to store the frequency of each character in string
            freq = {} # freq = {char: frequency}
            for char in string: # iterate through each character in string
                if char in freq: # if char is in freq
                    freq[char] += 1 # increment the frequency of char by 1
                else:
                    freq[char] = 1 # set the frequency of char to 1
            
            # Iterate through the keys in freq
            for key in freq:
                # If the frequency of the key is greater than 1, return False
                if freq[key] > 1:
                    return False
            
            # Return True
            return True
        
        # Create a function to find the maximum length of a concatenated string with unique characters
        def find_max_length(arr, string, index):
            # Base case: if index is equal to the length of arr, return the length of string
            if index == len(arr):
                return len(string)
            
            # Create a variable to store the maximum length of a concatenated string with unique characters
            max_length = 0
            
            # If the current string has unique characters, call find_max_length function with arr, string + arr[index], index + 1 as arguments and update max_length
            if has_unique_characters(string + arr[index]):
                max_length = max(max_length, find_max_length(arr, string + arr[index], index + 1))
            
            # Call find_max_length function with arr, string, index + 1 as arguments and update max_length
            max_length = max(max_length, find_max_length(arr, string, index + 1))
            
            # Return max_length
            return max_length
        
        # Call find_max_length function with arr, "", 0 as arguments and update max_length
        max_length = max(max_length, find_max_length(arr, "", 0))
        
        # Return max_length
        return max_length