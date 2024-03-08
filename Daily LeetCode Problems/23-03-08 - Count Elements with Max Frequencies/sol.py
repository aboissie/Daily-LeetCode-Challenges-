from collections import Counter
from typing import List 

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxCount = max(count.values())
        return maxCount * sum([1 for v in count.values() if v==maxCount])
        

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    output = 4

    print(Solution().maxFrequencyElements(nums=nums))