from collections import Counter 

class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        counter1 = Counter(word1).values()
        counter2 = Counter(word2).values()
        return list(sorted(counter1)) == list(sorted(counter2))
