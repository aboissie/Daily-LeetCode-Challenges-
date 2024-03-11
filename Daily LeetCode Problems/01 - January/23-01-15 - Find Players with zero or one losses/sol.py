from typing import List 
from collections import Counter 

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = [x[0] for x in matches], [x[1] for x in matches]
        parse = Counter(losers)
        return list(set(winners) - set(parse)), list(set([k for k,v in parse.items() if v==1]))
        