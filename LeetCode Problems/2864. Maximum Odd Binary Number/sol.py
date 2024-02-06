from typing import List 
import unittest

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """
        Return a string representing the maximum odd binary number that can be created from the given combination.
        """
        k = str.count(s, '1')
        n = len(s) 
        return '1' * (k - 1) + '0' * (n - k) + '1'