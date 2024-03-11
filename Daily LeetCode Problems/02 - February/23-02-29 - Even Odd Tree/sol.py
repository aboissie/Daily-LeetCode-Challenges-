from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.depthDic = {}
    
    def dfs(self, root, depth = 0):
        if not root:
            return True
        
        if depth in self.depthDic:
            if depth%2 == 0:
                if(root.val%2==1 and self.depthDic[depth] < root.val):
                    self.depthDic[depth] = root.val 
                else:
                    return False
            else:
                if(root.val%2==0 and self.depthDic[depth] > root.val):
                    self.depthDic[depth] = root.val 
                else:
                    return False
       
        else:
            if (root.val % 2) == ((depth + 1) % 2):
                self.depthDic[depth] = root.val   
            else:
                return False  

        a = self.dfs(root.left, depth + 1)
        b = self.dfs(root.right, depth + 1)
        
        return a and b and True


    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)
    
if __name__ == "__main__":
    tn = TreeNode(10)
    tn.left = TreeNode(10)
    tn.right = TreeNode(4)
    tn.right.right = TreeNode(3)
    
    print(Solution().isEvenOddTree(tn))