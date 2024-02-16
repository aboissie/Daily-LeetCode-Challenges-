from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        k = 0 
        while(nums[k] >= sum(nums[k+1:])):
            k = k + 1
            if k == len(nums):
                return -1
        return sum(nums[k:])
