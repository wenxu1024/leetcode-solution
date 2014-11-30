# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return head
        prev = head
        current = head.next
        lListDict = {}
        count = 1
        while current != None:
            if current.val == prev.val:
                count += 1
            else:
                if count > 1:
                    lListDict[prev.val] = True
                prev = current
                count = 1
            current = current.next
        if count > 1:
            lListDict[prev.val] = True
            
        current = head
        while current != None and current.val in lListDict:
            current = current.next
        head = current
        
        if head == None:
            return head
        current = head.next
        prev = head
        while current != None:
            if current.val not in lListDict:
                prev.next = current
                prev = current
            current = current.next
        prev.next = None
        return head
        

            
            
        
