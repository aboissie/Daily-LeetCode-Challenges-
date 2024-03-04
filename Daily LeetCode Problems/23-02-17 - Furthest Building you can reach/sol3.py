from typing import List 
import unittest 
import heapq

class Solution:      
   def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0: 
                heapq.heappush(jumps, diff)
                
            if(len(jumps) > ladders): 
                bricks -= heapq.heappop(jumps)

            if bricks < 0:
                return i 
        
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