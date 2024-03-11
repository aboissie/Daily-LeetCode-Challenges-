import unittest 
from typing import List 

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        res = []
        for i in range(len(digits)):
            for j in range(i+1, len(digits)+1):
                if low <= int(digits[i:j]) <= high:
                    res.append(int(digits[i:j]))

        return sorted(res)
    

