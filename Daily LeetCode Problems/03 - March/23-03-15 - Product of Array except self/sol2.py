from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Instead of storing arrays, use prefix/suffix sums
        arrf = 1
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            res[i] *= arrf
            arrf *= nums[i]

        arrf = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= arrf
            arrf *= nums[i]

        return res 
    
if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))