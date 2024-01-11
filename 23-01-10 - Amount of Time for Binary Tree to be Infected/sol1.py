class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, node):
        if node.val in self.nodes:
            return 
        self.nodes[node.val] = node
    
    def spreadInfection(self):
        currently_infected = [x.val for x in self.nodes.values() if x.infected]
        for node in currently_infected:
            for e in node.edges:
                self.nodes[e.val].infected = True

    def allInfected(self) -> bool:
        return all([x.infected for x in self.nodes.values()])
    
class Node:
    def __init__(self, node = TreeNode):
        self.edges = []
        self.val = node.val 
        self.node = node 
        self.infected = False 
        
    def addEdge(self, other: "Node"):
        self.edges.append(other)
        other.edges.append(self)
        
from typing import Optional 

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = Graph()
        def convertGraph(root):
            if root == None:
                return 
            
            g.addNode(Node(root))
            if root.left != None:
                g.addNode(Node(root.left)) 
                g[root.val].addEdge(g[root.left.val])
                convertGraph(root.left)

            if root.right != None:
                g.addNode(Node(root.right))
                g[root.val].addEdge(g[root.right.val])
                convertGraph(root.right)
        
        convertGraph(root)
        g.nodes[start].infected = True 
        iter = 0
        while(not g.allInfected()):
            iter += 1
            g.spreadInfection()

        return iter          