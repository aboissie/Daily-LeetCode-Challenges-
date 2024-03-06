class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while(s[l] == s[r]):
            if l == r:
                return 1
            
            c = s[l]

            while(l <= r and s[l] == c):
                l += 1

            while(l <= r and s[r] == c):
                r -= 1

        return r - l + 1
    
if __name__ == "__main__":
    s = "cabaabac" 
    print(Solution().minimumLength(s))