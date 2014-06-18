#! /usr/bin/python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
 
    def __repr__(self):
        s=''
        while self:
            if s=='':
		s+=str(self.val)
 	    else:
		s+='->'+str(self.val)
 	    self=self.next
        s+='->'+'None'
        return s

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        current=head
        for i in range(n):
            current=current.next
        if current==None:
            return head.next
        pointer=head
        while current:
            prev=pointer
            pointer=pointer.next
            current=current.next
        prev.next=pointer.next
        return head
            
if __name__=='__main__':
     sol=Solution()
     head=ListNode(1)
     node2=ListNode(2)
     node3=ListNode(3)
     node4=ListNode(4)
     node5=ListNode(5)
     head.next=node2
     node2.next=node3
     node3.next=node4
     node4.next=node5
     print head
     print sol.removeNthFromEnd(head,2)
