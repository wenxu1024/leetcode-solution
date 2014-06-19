# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head==None:
            return None
        visited={}
        if not head:
            return None
        copyhead=RandomListNode(head.label)
        visited[head]=copyhead
        copyprev=copyhead
        current=head.next
        while current:
            copycurrent=RandomListNode(current.label)
            visited[current]=copycurrent
            copyprev.next=copycurrent
            copyprev=copycurrent
            current=current.next
        visited[None]=None
        copycurrent=copyhead
        current=head
        while current:
            copycurrent.random=visited[current.random]
            current=current.next
            copycurrent=copycurrent.next
        return copyhead
            
            
            
            
