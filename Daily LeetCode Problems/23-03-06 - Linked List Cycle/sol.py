from typing import Optional 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise, hare = head, head 
        while(hare.next and hare.next.next):
            hare = hare.next.next 
            tortoise = tortoise.next 
            if(hare == tortoise): return True 

        return False 