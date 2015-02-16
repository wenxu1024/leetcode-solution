import java.util.*;
// copy list with random pointer

//
// * Definition for singly-linked list with a random pointer.
  class RandomListNode {
      int label;
      RandomListNode next, random;
      RandomListNode(int x) { this.label = x; }
  };
 //
public class Solution {
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    public RandomListNode copyRandomList(RandomListNode head) {
        // write your code here
        if (head == null) return null;
        Map m = new HashMap<RandomListNode, RandomListNode> ();
        RandomListNode headcopy = new RandomListNode(head.label);
        m.put(head, headcopy);
        RandomListNode current, prev, currentcopy;
        current = head.next;
        prev = headcopy;
        while (current != null) {
            currentcopy = new RandomListNode(current.label);
            m.put(current, currentcopy);
            prev.next = currentcopy;
            prev = currentcopy;
            current = current.next;
        }
        current = head;
        currentcopy = headcopy;
        while (current != null) {
            currentcopy.random = (RandomListNode) m.get(current.random);
            current = current.next;
            currentcopy = currentcopy.next;
        }
        return headcopy;
        
    }
}


