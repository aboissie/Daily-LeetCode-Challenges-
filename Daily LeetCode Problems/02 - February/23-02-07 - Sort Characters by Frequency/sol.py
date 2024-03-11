from collections import Counter 

class Solution:
    def frequencySort(self, s: str) -> str:
        countFreqs = Counter(s)
        res = ""
        for k, v in sorted(countFreqs.items(), key = lambda x:-x[1]):
            res += k * v

        return res 


if __name__ == "__main__":
    s = "treeeyooooook"
    print(Solution().frequencySort(s))