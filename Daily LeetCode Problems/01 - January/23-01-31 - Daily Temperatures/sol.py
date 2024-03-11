import unittest
from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n 
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tmp: 
                idx = stack.pop()
                res[idx] = i -idx 
            stack.append(i)
        
        return res 
    
class TestEvalDailyTemperatures(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for Daily Temperatures...")

    def test_case1(self):
        temperatures = [73,74,75,71,69,72,76,73]
        dailyTemperaturesOutput = Solution().dailyTemperatures(temperatures)
        output = [1,1,4,2,1,1,0,0]
        self.assertEqual(dailyTemperaturesOutput, output)

    def test_case2(self):
        temperatures = [30,40,50,60]
        dailyTemperaturesOutput = Solution().dailyTemperatures(temperatures)
        output = [1,1,1,0]
        self.assertEqual(dailyTemperaturesOutput, output)

    def test_case3(self):
        temperatures = [30,60,90]
        dailyTemperaturesOutput = Solution().dailyTemperatures(temperatures)
        output = [1,1,0]
        self.assertEqual(dailyTemperaturesOutput, output)

if __name__ == '__main__':
    unittest.main()
