from typing import List 
from collections import Counter 
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:      
            res["".join(sorted(s))].append(s)

        return list(res.values())
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))