public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head==null) return false;
        ListNode hare = head;
        ListNode tortoise = head;
        while(hare.next!=null && hare.next.next!=null){
            hare = hare.next.next;
            tortoise = tortoise.next; 
            if(hare == tortoise) return true;
        }
        return false;
    }
}