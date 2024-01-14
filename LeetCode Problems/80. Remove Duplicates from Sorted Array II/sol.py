from typing import Optional, List 
from collections import Counter 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        currPos = 0
        for i, (k, v) in enumerate(count.items()):
            nums[currPos] = k
            currPos += 1 
            if v >= 2:
                nums[currPos] = k
                currPos += 1 

        return currPos

if __name__ == "__main__":
    arr = [1,1,1,2,2,3]
    print(Solution().removeDuplicates(arr))