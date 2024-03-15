from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrf = [1]
        arrb = [1]

        for i in range(len(nums) - 1):
            arrf.append(arrf[-1] * nums[i])
            arrb.append(arrb[-1] * nums[len(nums) - i - 1])

        return [arrb[len(nums) - i - 1] * arrf[i] for i in range(len(nums))]

if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))