from typing import List 
from collections import Counter 
from collections import defaultdict

class Solution:
    @staticmethod
    def hashString(s: str):
        res = [0] * 26
        count = Counter(s)  
        for k in count:
            res[ord(k) - ord('a')] = count[k]

        return tuple(res)
 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = Counter(s)        
            res[Solution.hashString(s)].append(s)

        return list(res.values())
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))