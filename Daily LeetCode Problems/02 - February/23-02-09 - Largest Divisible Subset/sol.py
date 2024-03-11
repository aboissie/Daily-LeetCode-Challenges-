from typing import List 

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        encountered = set()
        largest = []

        for num in nums:
            if num in encountered:
                continue 

            
            

        
if __name__ == "__main__":
    print(Solution().largestDivisibleSubset([1, 2, 3, 4]))