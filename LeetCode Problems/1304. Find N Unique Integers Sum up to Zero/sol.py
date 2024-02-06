from typing import List 
import unittest

class Solution:
    def sumZero(self, n: int) -> List[int]:
        """ 
        Given an integer `n`, return any array containing `n` unique integers such that they add up to 0.
        """
        if n  % 2 == 0:
            return list(range(1, n//2 + 1)) + list(range(-1, -n//2 - 1, -1))

        return  list(range(0, (n-1)//2 + 1)) + list(range(-1, -(n-1)//2 - 1, -1)) 

class TestEvalMinimumIndexSumTwoLists(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for Sum Zero...")

    def test_case1(self):
        print(Solution().sumZero(5))
        self.assertEqual(sum(Solution().sumZero(5)), 0)

    def test_case2(self):
        self.assertEqual(sum(Solution().sumZero(4)), 0)

if __name__ == "__main__":
    print(Solution().sumZero(5))
    unittest.main()