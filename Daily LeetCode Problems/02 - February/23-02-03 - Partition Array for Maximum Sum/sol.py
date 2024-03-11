from typing import List 

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (k + 1)

        for i in range(n - 1, -1, -1):
            currMax = 0
            end = min(n, i + k)

            for j in range(i, end):
                currMax = max(currMax, arr[j])
                dp[i % (k + 1)] = max(dp[i % (k + 1)], dp[(j + 1) % (k + 1)] + currMax * (j - i + 1))

        return dp[0]

if __name__=="__main__":
    arr = [1,15,7,9,2,5,10]
    k = 3
    print(Solution().maxSumAfterPartitioning(arr, k))