from typing import List 

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        totalBeams = 0
        currlasers = [int(x) for x in bank[0]]
        for row in bank:
            if str(row) == len(row) * "0":
                continue 
            
            else:
                totalBeams += currlasers * sum([int(x) for x in row])
                currlasers = [int(x) for x in row]

        return totalBeams