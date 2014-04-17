# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1 : return l2
        if not l2 : return l1
        carry=0
        d=l1.val+l2.val+carry
        if d>=10:
            carry=1
            d=d-10
        else:
            carry=0
        l=ListNode(d)
        head=l
        prev=l
        l1=l1.next
        l2=l2.next
        while l1 and l2:
            d=l1.val+l2.val+carry
            if d>=10:
                carry=1
                d=d-10
            else:
                carry=0
            l=ListNode(d)
            prev.next=l
            l1=l1.next
            l2=l2.next
            prev=l
        if l1:
            while l1:
                d=l1.val+carry
                if d>=10:
                    carry=1
                    d=d-10
                else:
                    carry=0
                l=ListNode(d)
                prev.next=l
                l1=l1.next
                prev=l
        else:
            while l2:
                d=l2.val+carry
                if d>=10:
                    carry=1
                    d=d-10
                else:
                    carry=0
                l=ListNode(d)
                prev.next=l
                l2=l2.next
                prev=l
        if carry:
            l=ListNode(carry)
            prev.next=l
            prev=l
        else:
            pass
        return head
            
        
