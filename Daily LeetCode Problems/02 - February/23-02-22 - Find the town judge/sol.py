from typing import List 
from collections import defaultdict 

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = defaultdict(list)
        trusters = set()
        for a, b in trust:
            dic[b].append(a)
            trusters.add(a)

        judge = -1
        for a in dic:
            if len(dic[a]) == n - 1 and a not in trusters:
                if judge == -1:
                    judge = a 
                else:
                    return -1
                
        return judge

if __name__=="__main__":
    n = 3
    trust = [[1,3],[2,3]]

    print(Solution().findJudge(n, trust))