from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        all_subarrays = []
        
        def dfs(i):
            if i == len(arr):
                return 
            
            for j in range(i, len(arr)):
                all_subarrays.append(arr[i:j+1])
                dfs(j+1)
        
        dfs(0)
        print(all_subarrays)
            

        x = set([5])
        x.add()