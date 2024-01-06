#include <vector> // for vector
#include <algorithm> // for sort
#include <iostream> // for debugging


using namespace std;

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) { // function to find the maximum profit you can achieve from these jobs
        int n = startTime.size();
        vector<vector<int>> jobs(n, vector<int>(3));
        for (int i = 0; i < n; ++i) {
            jobs[i] = {endTime[i], startTime[i], profit[i]};
        }
        sort(jobs.begin(), jobs.end());

        vector<int> dp(n);
        dp[0] = jobs[0][2];
        for (int i = 1; i < n; ++i) {
            int l = -1;
            int r = i - 1;
            while (l < r) {
                int mid = l + (r - l + 1) / 2;
                if (jobs[mid][0] <= jobs[i][1]) {
                    l = mid;
                } else {
                    r = mid - 1;
                }
            }
            if (l == -1) { // no job before this one
                dp[i] = max(jobs[i][2], dp[i - 1]); // take the current job or not
            } else { // take the current job or not
                dp[i] = max(jobs[i][2] + dp[l], dp[i - 1]); // take the current job or not
            }
        }
        return dp[n - 1];
    }
};

int main() {
    Solution sol;

    // Existing test case
    vector<int> startTime1 = {1,2,3,3};
    vector<int> endTime1 = {3,4,5,6};
    vector<int> profit1 = {50,10,40,70};
    cout << "Expected: 120, Got: " << sol.jobScheduling(startTime1, endTime1, profit1) << endl;

    // New test case
    vector<int> startTime2 = {1,2,3,4,6};
    vector<int> endTime2 = {3,5,10,6,9};
    vector<int> profit2 = {20,20,100,70,60};
    cout << "Expected: 150, Got: " << sol.jobScheduling(startTime2, endTime2, profit2) << endl;

    return 0;
}