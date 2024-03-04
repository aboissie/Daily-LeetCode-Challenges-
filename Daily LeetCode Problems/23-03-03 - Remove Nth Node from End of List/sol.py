from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def LinkedListLength(head: Optional[ListNode])->int:
        dummy = ListNode(0, next = head)
        curr = dummy.next 
        length = 0
        while(curr != None): length, curr = length + 1, curr.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, next = head)
        curr = dummy.next 
        
        currentNode = 0
        length = Solution().LinkedListLength(head)

        while(length - currentNode < n):
            curr = curr.next 
            
        curr = curr.next
        return dummy.next 

if __name__ == "__main__":
    ln = ListNode(0)
    ln.next = ListNode(1)
    ln.next.next = ListNode(2)
    ln.next.next.next = ListNode(3)
    ln.next.next.next.next = ListNode(4)

    print(Solution().LinkedListLength(ln))
    print(Solution().removeNthFromEnd(ln, 5))
    print("BON")

