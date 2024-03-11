#include <vector>

class Solution {
public:
    static const int M = 1000000007;
    std::vector<std::vector<std::vector<int>>> dp;
    int m_, n_;

    int findPaths(int m, int n, int maxMove, int x, int y) {
        m_ = m;
        n_ = n;
        dp.assign(m, std::vector<std::vector<int>>(n, std::vector<int>(maxMove + 1, -1)));

        return helper(maxMove, x, y);
    }

    int helper(int maxMove, int x, int y) {
        if (x < 0 || x >= m_ || y < 0 || y >= n_) return 1;
        if (maxMove <= 0) return 0;
        if (dp[x][y][maxMove] != -1) return dp[x][y][maxMove]; // Check for precomputed value

        int res = 0;
        res = (res + helper(maxMove - 1, x + 1, y)) % M;
        res = (res + helper(maxMove - 1, x - 1, y)) % M;
        res = (res + helper(maxMove - 1, x, y - 1)) % M;
        res = (res + helper(maxMove - 1, x, y + 1)) % M;

        dp[x][y][maxMove] = res; 
        return res;
    }
};
