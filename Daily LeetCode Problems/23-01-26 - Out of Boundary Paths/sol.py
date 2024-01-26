class Solution:
    def __init__(self):
        self.res = 0

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(i, j, moves):            
            if i < 0 or j < 0 or i >= m or j >= n:
                self.res += 1
                return 

            if moves == 0:
                return 0

            dfs(i+1, j, moves-1)
            dfs(i-1, j, moves-1)
            dfs(i, j+1, moves-1)
            dfs(i, j-1, moves-1)

        dfs(startRow, startColumn, maxMove)
        return self.res % ((10**9) + 7)