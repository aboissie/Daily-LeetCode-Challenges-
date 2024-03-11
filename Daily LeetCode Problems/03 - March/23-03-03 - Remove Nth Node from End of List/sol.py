from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

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

