import unittest

class Solution:
    @staticmethod
    def checkSubstring(stringA: str, stringB: str) -> bool:
        # Create a frequency map for all characters in stringB
        char_frequency = {}
        for char in stringB:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
        
        # Check if stringA contains all characters from stringB with at least the same frequency
        for char in stringB:
            if char not in stringA or stringA.count(char) < char_frequency[char]:
                return False
        
        return True
 
    def minWindow(self, s: str, t: str) -> str:
        if not Solution.checkSubstring(s, t):
            return ""
        
        min_len = float('inf')
        min_window = ""
        
        for left in range(len(s)):
            for right in range(left + len(t), len(s) + 1):
                window = s[left:right]
                if Solution.checkSubstring(window, t) and len(window) < min_len:
                    min_len = len(window)
                    min_window = window
                    break  # Break the inner loop as soon as the condition is met to avoid unnecessary checks
        
        return min_window
        
class TestminWindow(unittest.TestCase):
    def setUp(self):
        print(f"Running {self._testMethodName} for minimum window substring ...")

    def test_case1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(Solution().minWindow(s, t), "BANC")

    def test_case2(self):
        s = "a"
        t = "a"
        self.assertEqual(Solution().minWindow(s, t), "a")
    
    def test_case3(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(Solution().minWindow(s, t),"BANC")

    def test_case4(self):
        s = "acbbaca"
        t = "aba"
        self.assertEqual(Solution().minWindow(s, t), "baca")

        
if __name__=="__main__":
    unittest.main()