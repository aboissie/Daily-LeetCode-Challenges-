from typing import List 
from collections import Counter 
import unittest

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqCount = Counter(arr)
        remain = k
        res = 0

        for key, value in sorted(freqCount.items(), key = lambda x:x[1]):
            if remain >= value:
                remain -= value 
                value = 0
                res += 1
            
            else: 
                break 
            
        return len(freqCount) - res


class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for {Solution.findLeastNumOfUniqueInts.__name__}...")

    def test_case1(self):
        arr = [5,5,4]
        k = 1
        output = 1
        self.assertEqual(Solution().findLeastNumOfUniqueInts(arr, k), output)

    def test_case2(self):
        arr = [4,3,1,1,3,3,2]
        k = 3
        output = 2
        self.assertEqual(Solution().findLeastNumOfUniqueInts(arr, k), output)

    def test_case3(self):
        arr = [2,1,1,3,3,3]
        k = 3 
        output = 1
        self.assertEqual(Solution().findLeastNumOfUniqueInts(arr, k), output)

if __name__ == '__main__':
    unittest.main()