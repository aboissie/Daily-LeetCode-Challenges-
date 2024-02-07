from collections import Counter 

class Solution:
    def frequencySort(self, s: str) -> str:
        countFreqs = Counter(s)
        return "".join([k*v for k, v in countFreqs.most_common()])


if __name__ == "__main__":
    s = "treeeyooooook"
    print(Solution().frequencySort(s))