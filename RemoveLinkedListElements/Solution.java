/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode current, prev;
        current = head;
        prev = null;
        while(current != null) {
            if (current.val == val) {
                current = current.next;
            }
            else {
                if (prev == null) {
                    head = current;
                    prev = current;
                }
                else {
                    prev.next = current;
                    prev = current;
                }
                current = current.next;
            }
        }
        if (prev == null) {
            head = current;
            prev = current;
        }
        else {
            prev.next = current;
            prev = current;
        }
        return head;
    }
}
