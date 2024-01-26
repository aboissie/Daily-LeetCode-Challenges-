class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int M = 1000000007; // Correct modulo operation
        int[][] dp = new int[m][n];
        dp[startRow][startColumn] = 1;

        int res = 0;

        for(int moves = 1; moves <= maxMove; moves++){ // Include maxMove
            int[][] tmp = new int[m][n];
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    // Only add to res on the first move
                    if (moves == 1) {
                        if (i == m - 1) res = (res + dp[i][j]) % M;
                        if (j == n - 1) res = (res + dp[i][j]) % M;
                        if (i == 0) res = (res + dp[i][j]) % M;
                        if (j == 0) res = (res + dp[i][j]) % M;
                    }

                    long count = 0;
                    if (i > 0) count = (count + dp[i - 1][j]) % M;
                    if (i < m - 1) count = (count + dp[i + 1][j]) % M;
                    if (j > 0) count = (count + dp[i][j - 1]) % M;
                    if (j < n - 1) count = (count + dp[i][j + 1]) % M;

                    tmp[i][j] = (int) count;
                }
            }
            dp = tmp;
        }

        return res;
    }
}
