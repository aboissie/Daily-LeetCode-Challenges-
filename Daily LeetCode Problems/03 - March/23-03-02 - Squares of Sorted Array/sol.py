from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        posIdx = len(nums)
        for i, n in enumerate(nums):
            if n >= 0: 
                posIdx = i
                break
        
        res = []
        negCurr = posIdx - 1
        posCurr = posIdx 

        while(posCurr < len(nums) and negCurr >= 0):
            if(nums[posCurr] < - nums[negCurr]):
                res.append(nums[posCurr])
                posCurr += 1
            else:
                res.append(-nums[negCurr])
                negCurr -= 1

        # If negCurr == -1: we have exhausted all negative values, so simply append the positive ones
        if(negCurr == -1):
            res = res + nums[posCurr:]

        # Otherwise, we simply add all remaining negative values
        else:
            res = res + nums[:negCurr+1][::-1]

        return [k**2 for k in res]
        
            
if __name__ == "__main__":
    nums = [-1]
    print(Solution().sortedSquares(nums))