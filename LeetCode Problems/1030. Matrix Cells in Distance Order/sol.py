from typing import List
from collections import defaultdict 

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        V = defaultdict(list)
        for y in range(rows):
            dy = abs(y - rCenter)
            for x in range(cols):
                m = dy + abs(x - cCenter)
                V[m].append((y, x))

        res = []
        for v in sorted(V):
             res.extend(V[v])
        return res
        
    
if __name__ == '__main__':
	print(Solution().allCellsDistOrder(2, 3, 1, 2))