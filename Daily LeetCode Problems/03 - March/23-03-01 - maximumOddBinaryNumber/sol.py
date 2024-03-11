class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if s.find("1") == -1:
            return s
        n = len(s)
        k = s.count("1")
        
        return "1" * (k - 1) + "0" * (n - k) + "1"
        
        

if __name__ == "__main__":
    s = "000"
    print(Solution().maximumOddBinaryNumber(s))
    s = "111"
    print(Solution().maximumOddBinaryNumber(s))