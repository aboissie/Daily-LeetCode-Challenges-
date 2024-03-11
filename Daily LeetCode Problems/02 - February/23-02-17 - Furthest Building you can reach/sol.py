from typing import List 
import unittest 

class Solution:
    @staticmethod 
    def furthestBuildingHelper(heights, bricks, ladders, current)->int:
        if len(heights) == 1:
            return current 
        
        if heights[1] < heights[0]:
                return Solution.furthestBuildingHelper(heights[1:], bricks, ladders, current + 1)
        
        if ladders == 0:
             if bricks < heights[1] - heights[0]:
                  return current 
             
             else:
                  diffBrick = max(0, heights[1] - heights[0])
                  return Solution.furthestBuildingHelper(heights[1:], bricks - diffBrick, ladders, current + 1)

        if bricks < heights[1] - heights[0]:
            return Solution.furthestBuildingHelper(heights[1:], bricks, ladders - 1, current + 1)

        diffBrick = max(0, heights[1] - heights[0])
        sol1 = Solution.furthestBuildingHelper(heights[1:], bricks - diffBrick, ladders, current + 1)
        sol2 = Solution.furthestBuildingHelper(heights[1:], bricks, ladders - 1, current + 1)
        return max(sol1, sol2)
            
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        return Solution.furthestBuildingHelper(heights, bricks, ladders, 0)

if __name__=="__main__":
    heights = [4,12,2,7,3,18,20,3,19]
    bricks = 10
    ladders = 2

    print(Solution().furthestBuilding(heights, bricks, ladders))

    heights = [14,3,19,3]
    bricks = 17
    ladders = 0

    print(Solution().furthestBuilding(heights, bricks, ladders))