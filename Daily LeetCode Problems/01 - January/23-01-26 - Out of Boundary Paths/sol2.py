class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        res = 0

        for move in range(1, maxMove + 1):  # Include maxMove in the range
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if move == maxMove:  # Update res only when move equals maxMove
                        if i == m - 1: res = (res + dp[i][j]) % M
                        if i == 0: res = (res + dp[i][j]) % M
                        if j == 0: res = (res + dp[i][j]) % M
                        if j == n - 1: res = (res + dp[i][j]) % M
                    if i > 0:
                        tmp[i][j] += dp[i - 1][j] % M
                    if i < m - 1:
                        tmp[i][j] += dp[i + 1][j] % M
                    if j > 0:
                        tmp[i][j] += dp[i][j - 1] % M
                    if j < n - 1:
                        tmp[i][j] += dp[i][j + 1] % M

            dp = tmp

        return res
