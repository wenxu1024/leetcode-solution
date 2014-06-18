# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        current=head
        visited={}
        while current:
            if current in visited:
                return current
            visited[current]=True
            current=current.next
        else:
            return None
        
