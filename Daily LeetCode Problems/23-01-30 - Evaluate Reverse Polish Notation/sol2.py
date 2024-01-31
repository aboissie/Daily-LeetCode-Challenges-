from typing import List
import unittest

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '/', '*']:
                a, b = stack.pop(), stack.pop()
                if token == '/':
                    stack.append(int(b/a))
                elif token == '*':
                    stack.append(b*a)
                elif token == '+':
                    stack.append(b+a)
                elif token == '-':    
                    stack.append(b-a)
            
            else: 
                stack.append(int(token))
                
        return stack.pop()
    
class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for RPN...")

    def test_case1(self):
        tokens = ["2", "1", "+", "3", "*"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 9)

    def test_case2(self):
        tokens = ["4", "13", "5", "/", "+"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 6)

    def test_case3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        result = Solution().evalRPN(tokens)
        self.assertEqual(result, 22)

if __name__ == '__main__':
    unittest.main()
