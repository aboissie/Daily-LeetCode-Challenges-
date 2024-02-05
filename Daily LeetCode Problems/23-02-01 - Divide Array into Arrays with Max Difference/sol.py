
import unittest 
from typing import List 

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = [[]]        
        for num in sorted(nums):
            currentBucket = res[-1]
            minElement = min(currentBucket) if currentBucket else num
            if len(currentBucket) < 3:
                if abs(num - minElement) > k: return []
                res.append(res.pop() + [num])
                continue 
            
            res.append([num])

        return res if len(res[-1])==3 else []
    
class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for Divide Array into Arrays w/ Max Diff...")

    def test_case1(self):
        nums = [1,3,4,8,7,9,3,5,1]
        k = 2
        output = [[1,1,3],[3,4,5],[7,8,9]]
        self.assertEqual(Solution().divideArray(nums, k), output)

    def test_case2(self):
        nums = [1,3,3,2,7,3]
        k = 3
        output = []
        self.assertEqual(Solution().divideArray(nums, k), output)


if __name__ == '__main__':
    unittest.main()
