# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lA = self.lenLinkedList(headA)
        lB = self.lenLinkedList(headB)
        currentA = headA
        currentB = headB
        if lA > lB:
            d = lA - lB
            current = headA
            while d > 0:
                current = current.next
                d -= 1
            currentA = current
        elif lA < lB:
            d = lB - lA
            current = headB
            while d > 0:
                current = current.next
                d -= 1
            currentB = current
        else:
            pass
        while currentA != currentB and currentA != None:
            currentA = currentA.next
            currentB = currentB.next
        return currentA
                
        
        
    def lenLinkedList(self, head):
        l = 0
        current = head
        while current != None:
            l += 1
            current = current.next
        return l
