class Solution {
    public ListNode deleteDupicates(ListNode head){
        if(head == null) return head;
        ListNode pre = head;

        ListNode next = head.next;

        while(next != null) {
            if (pre.val != next.val) {
                pre = next;
                next = next.next;
            } else {
                pre.next = next.next;
                next = next.next;
            }
        }
        return head;
    }
}