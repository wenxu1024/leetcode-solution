#! /usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        l = len(lists)
        A = []
        for i in range(l):
            if lists[i] != None:
                self.heapinsert(A, lists[i]) #create a heap
#        print A[0].val, A[1].val, A[2].val, A[3].val
        if A == []: #if heap empty, return None
            return None
        head = A[0] # the minium is Linked List head
        while A != []: # if the heap empty, stop
            current = self.heappop(A) # get current ListNode from heap, and remove from heap
            if current.next != None:
                self.heapinsert(A, current.next)  # if current.next is not empty, add to the heap
            if A == []: # if heap is empty, we finish
                return head
            else: # else, next node is the miniumum
                nextnode = A[0]
            current.next = nextnode # Link the current node, to the next node
        return head
            
            
            
        
    
    def heapinsert(self, A, node):
        A.append(node)
        self.siftUp(A)
    
    def heappop(self, A):
        temp = A[0]
        A[0] = A[-1]
        A[-1] = temp
        node = A.pop()
        self.siftDown(A)
        return node
        
    def siftDown(self, A):
        l = len(A)
        if l <= 1:
            return
        i = 0
        while (i <= (l - 1) / 2):
            k1 = 2 * i + 1
            k2 = 2 * i + 2
            if k2 <= l - 1:
                A[k1]
                A[k2]
                A[i]
                if A[i].val <= A[k1].val and A[i].val <= A[k2].val:
                    break
                else:
                    if A[k1].val < A[k2].val:
                        temp = A[i]
                        A[i] = A[k1]
                        A[k1] = temp
                        i = k1
                    else:
                        temp = A[i]
                        A[i] = A[k2]
                        A[k2] = temp
                        i = k2
            elif k1 <= l - 1:
                if A[i].val <= A[k1].val:
                    break
                else:
                    temp = A[i]
                    A[i] = A[k1]
                    A[k1] = temp
                    i = k1
            else:
                return
        
        
    def siftUp(self, A):
        l = len(A)
        i = l - 1
        while (i >= 1):
            k = (i - 1) / 2
            if A[i].val < A[k].val:
                temp = A[i]
                A[i] = A[k]
                A[k] = temp
                i = k
            else:
                break



if __name__ == "__main__":
    head = ListNode(0)
    node1 = ListNode(2)
    node2 = ListNode(5)
    node3 = ListNode(4)
   # head.next = node1
   # node1.next = node2
    sol = Solution()
    newhead = sol.mergeKLists([head,node3,node2,node1 ])
    print newhead.val, newhead.next.val, newhead.next.next.val, newhead.next.next.next.val
