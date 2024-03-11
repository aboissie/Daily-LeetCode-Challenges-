import unittest 
from typing import List

class Solution:    
    @staticmethod
    def dfs(res, k):
        return Solution.dfs(res + str(int(res[-1]) + 1), k - 1) if k > 0 else res
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n = len(str(low))        
        m = len(str(high))
        res = []
        for k in range(n - 1, m):
            for firstDigit in range(1, 10 - k):
                curr = int(Solution.dfs(str(firstDigit), k))
                if curr >= low and curr <= high:
                    res.append(curr)
            k += 1
        return sorted(res)
    

class TestEvalsequentialDigits(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for Sequential Digits ...")

    def test_case1(self):
        low = 100
        high = 300
        output = [123,234]
        self.assertEqual(Solution().sequentialDigits(low, high), output)

    def test_case2(self):
        low = 1000
        high = 13000
        output = [1234,2345,3456,4567,5678,6789,12345]

        self.assertEqual(Solution().sequentialDigits(low, high), output)

if __name__=="__main__":
    unittest.main()
