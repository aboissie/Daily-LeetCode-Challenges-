class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        for item in order:
            res += s.count(item) * item
            s = s.replace(item, "")

        return res + s
    
if __name__ == "__main__":
    order = "kqep"
    s = "pekeq"
    
    print(Solution().customSortString(order, s))