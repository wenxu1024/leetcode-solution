/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode current;
        int l;
        l = 0;
        current = head;
        while(current != null) {
            l ++;
            current = current.next;
        }
        if (l <= 1) return true;
        int half = l / 2;
        ListNode prev, temp;
        current = head;
        for(int i = 0; i < (l + 1) / 2; i ++) {
            current = current.next;
        }
        prev = null;
        while(current != null) {
            temp = current.next;
            current.next = prev;
            prev = current;
            current = temp;
        }
        ListNode head2 = prev;
        ListNode current2;
        current2 = head2;
        current = head;
        while(current2 != null) {
            if (current2.val != current.val) return false;
            current2 = current2.next;
            current = current.next;
        }
        return true;
    }
}
