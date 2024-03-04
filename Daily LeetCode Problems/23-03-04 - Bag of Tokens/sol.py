from typing import List 

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int, score = 0) -> int:
        if not tokens:
            return score
        
        sortedTokens = tokens

        while(sortedTokens and power >= sortedTokens[0]):
            power -= sortedTokens[0]
            score += 1
            sortedTokens.pop(0)

        print(sortedTokens)
        print(score)


        return max(score, self.bagOfTokensScore(sortedTokens[:-1], power + (sortedTokens[-1] if sortedTokens else 0), score - 1) if score >= 1 else 0)
            
if __name__ == "__main__":
    tokens = [71,55,82]
    power = 54
    print(Solution().bagOfTokensScore(tokens, power))