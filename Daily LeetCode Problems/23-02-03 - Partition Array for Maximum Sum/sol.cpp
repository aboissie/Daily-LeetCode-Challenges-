#include <vector>
using namespace std;

class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(k + 1, 0);
        for(int i = 0; i < arr.size(); i ++){
            int currMax = 0;
            int end = max(n, i + k);
            for(int j = i; j < end; j++){
                dp[i % (k + 1)] = 
            }
        }
    }
};