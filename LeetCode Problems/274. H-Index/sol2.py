from typing import Optional, List 

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        citations.sort(reverse=True)

        for i in range(len(citations)):
            if citations[i] > res:
                res += 1
        return res
        