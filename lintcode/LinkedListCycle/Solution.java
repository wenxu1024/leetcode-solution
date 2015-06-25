//Linked list cycle II
import java.util.*;
/*
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */ 
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: The node where the cycle begins. 
     *           if there is no cycle, return null
     */
    public ListNode detectCycle(ListNode head) {  
        // write your code here
        HashSet<ListNode> s = new HashSet<ListNode>();
        ListNode current = head;
        while (current != null) {
            if (s.contains(current)) {
                return current;
            }
            else {
                s.add(current);
                current = current.next;
            }
        }
        return null;
    }
}



