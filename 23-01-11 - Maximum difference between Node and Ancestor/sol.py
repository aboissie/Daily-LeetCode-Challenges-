from typing import Optional 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right

class Solution:
    @staticmethod
    def __helper(root: TreeNode, currmin: int, currmax: int):
        if not root:
            return currmax - currmin 
        
        currmin = min(root.val, currmin)
        currmax = max(root.val, currmax)
        
        left = Solution.__helper(root.left, currmin, currmax)
        right = Solution.__helper(root.right, currmin, currmax)

        return max(left, right)
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return Solution.__helper(root, root.val, root.val)
        

    