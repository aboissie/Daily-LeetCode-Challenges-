from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for k, v in Counter(s).items():
            if v==1:
                return s.find(k)
        return -1