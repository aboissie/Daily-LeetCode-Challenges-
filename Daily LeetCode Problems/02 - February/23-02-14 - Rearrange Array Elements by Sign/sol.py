from typing import List 

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        stack1 = [k for k in nums if k>0]
        stack2 = [k for k in nums if k<0]
        res = []
        for num1, num2 in zip(stack1, stack2):
            res.append(num1)
            res.append(num2)
        
        return res 

if __name__=="__main__":
    nums = [-1,1]
    print(Solution().rearrangeArray(nums))