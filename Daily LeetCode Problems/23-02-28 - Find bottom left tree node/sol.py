from typing import Optional
from collections import defaultdict 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.dic = defaultdict(list)

    def findBottomLeftValueHelper(self, root: Optional[TreeNode], k = 0) -> int:
        if not root:
            return None 
        
        self.dic[k].append(root.val)
        self.findBottomLeftValueHelper(root.left, k + 1)
        self.findBottomLeftValueHelper(root.right, k + 1)
                
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.findBottomLeftValueHelper(root, 0)
        return self.dic[max(self.dic)][0]
    
if __name__ == "__main__":
    tn = TreeNode(0)
    tn.left = TreeNode(1)
    tn.right = TreeNode(2)
    tn.right.right = TreeNode(3)
    tn.left.left = TreeNode(5)

    print(Solution().findBottomLeftValue(tn))
    
