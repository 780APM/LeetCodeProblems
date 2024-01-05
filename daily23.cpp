/* Longest Increasing Subsequence

/* Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4

Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

constraits 
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        int ans = 1;
        for(int i = 1; i < n; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            ans = max(ans, dp[i]);
        }
        return ans;
    }
};

int main() {
    Solution sol;

    // Existing test case
    vector<int> nums1 = {10,9,2,5,3,7,101,18};
    cout << "Expected: 4, Got: " << sol.lengthOfLIS(nums1) << endl;

    // New test case
    vector<int> nums2 = {0,1,0,3,2,3};
    cout << "Expected: 4, Got: " << sol.lengthOfLIS(nums2) << endl;

    return 0;
}