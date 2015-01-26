#! /usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        current = self
        s = ""
        while current.next != None:
	    s = s + str(current.val) + '->'
            current = current.next
 	s = s + str(current.val) 
        return s

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        current = head
        if head == None:
            return None
        prev = None
        for i in range(k):
            if current != None:
                current = current.next
            else:
                return head
                break
        else:
            current = head
            for i in range(k):
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            head2 = self.reverseKGroup(current, k)
            head = prev
            current = head
            while current.next != None:
                current = current.next
            current.next = head2
            return head
            
if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print head
    sol = Solution()
    k = 2
    head = sol.reverseKGroup(head, 2)
    print head
    

