import math 
from collections import defaultdict

class Solution:
    @staticmethod
    def createPerfectSquares(n:int) -> dict:
        maxPerfect = int(math.sqrt(n) + 1)
        return [k**2 for k in range(1, maxPerfect)]

    def numSquaresHelper(self, n: int, dic: dict) -> int:
        if n in dic:
            return dic[n]
        
        dic[n] = float('inf')
        for k in Solution.createPerfectSquares(n):
            self.numSquaresHelper(n - k, dic)
            dic[n] = min(dic[n], 1 + dic[n - k])
            
        
        return dic[n]
        
    def numSquares(self, n: int) -> int:
        return self.numSquaresHelper(n, {0:0, 1: 1})
        
if __name__=="__main__":
    print(Solution().numSquares(12))