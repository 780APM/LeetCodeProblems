# Element appearing more than 25% in sorted array. Return the element that appears more than 25% of the time.

class Solution(object):
    def findSpecialInteger(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # 1. Calculate the window size
        window_size = len(arr) // 4 + 1

        # 2. Iterate over the array with a sliding window
        for i in range(len(arr) - window_size + 1):
            # 3. If the first element of the window is the same as the last, return that element
            if arr[i] == arr[i + window_size - 1]:
                return arr[i]
        # If no element is found, return -1 or any other value indicating failure
        return -1

# create a test case

    arr = [1,2,2,6,6,6,6,7,10]
    print(findSpecialInteger(arr))

