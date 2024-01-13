from collections import Counter 

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1 = Counter(s)
        t1 = Counter(t)
        
        return sum([x for x in (s1 - t1).values()])
        

if __name__ == "__main__":
    s = "anagram"
    t = "mangzzr"
    
    Solution().minSteps(s, t)