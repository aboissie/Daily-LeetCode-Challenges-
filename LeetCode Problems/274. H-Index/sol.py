from typing import Optional, List 
from collections import Counter 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = Counter(citations)
        maxH = 0

        while(True):
            if sum([count.get(k) for k in range(maxH + 1, max(citations))]) >= maxH + 1:
                maxH += 1
            else:
                break 

        return maxH