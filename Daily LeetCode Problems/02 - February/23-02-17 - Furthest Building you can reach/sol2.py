from typing import List 
import unittest 
import heapq

class Solution:      
   def canReach(self, pos: int, bricks: int, ladders: int, jumps: int)->bool:
        maxjumps = heapq.nlargest(min(ladders, pos), jumps[:pos])
        for k in jumps:
            if k in maxjumps and ladders>0:
                ladders-=1
                pos-=1

            elif bricks >= k:
                bricks-=k 
                pos-=1
            
            else:
                break 
        
        return (pos <= 0)
    
   def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps = []
        for i in range(len(heights) - 1):
            jumps.append(max(heights[i + 1] - heights[i], 0))

        l = 0
        r = len(heights)
        while(l <= r):
            c = (r + l)//2
            if self.canReach(c + 1, bricks, ladders, jumps):
                l = c + 1 
            elif self.canReach(c, bricks, ladders, jumps):
                return c 
            else:
                r = c - 1

        return len(heights) - 1
            
if __name__=="__main__":
    heights = [4,12,2,7,3,18,20,3,19]
    bricks = 10
    ladders = 2

    print(Solution().furthestBuilding(heights, bricks, ladders))

    heights = [14,3,19,3]
    bricks = 17
    ladders = 0

    print(Solution().furthestBuilding(heights, bricks, ladders))