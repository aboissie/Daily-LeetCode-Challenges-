from collections import Counter 
from typing import List 

class Solution:
    from collections import Counter

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values()))==len(Counter(arr).values())
