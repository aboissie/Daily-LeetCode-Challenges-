from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def bfs(root1: Optional[TreeNode]) -> list:
    tovisit = deque()
    tovisit.append(root1)

    res = []
    while(len(tovisit) > 0):
        r = tovisit.pop()
        if(r.left == None and r.right == None):
            res.append(r.val)
            continue 
        
        if(r.left != None):
            tovisit.append(r.left)
        if(r.right != None):
            tovisit.append(r.right)
            
    return res

def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    return bfs(root1) == bfs(root2)