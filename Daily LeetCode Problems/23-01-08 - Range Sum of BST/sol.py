from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        
        acc = 0 

        if root.val <= high and root.val >= low:
            acc += root.val 
            
        acc += self.rangeSumBST(root.left, low, high)
        acc += self.rangeSumBST(root.right, low, high)

        return acc