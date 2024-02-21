class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = '{0:31b}'.format(right)
        r = '{0:31b}'.format(left)
        
        res = ""
        nomatch = True
        for i, j in zip(l, r):
            if i == j and nomatch:
                res += i 
                continue 
            res += "0"
            nomatch = False 

        return int(res.strip(" "), base = 2)


if __name__ == "__main__":
    left = 1
    right = 2147483647
    print(Solution().rangeBitwiseAnd(left, right))
    