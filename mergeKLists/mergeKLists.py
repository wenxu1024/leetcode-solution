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
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        l=len(lists)
        if l==0:
            return None
        if l==1:
            return lists[0]
        leftList=self.mergeKLists(lists[:l/2])
        rightList=self.mergeKLists(lists[l/2:])
        head=self.mergetwoLists(leftList,rightList)
        return head
        
    def mergetwoLists(self,leftList,rightList):
        if leftList==None:
            return rightList
        if rightList==None:
            return leftList
        if leftList.val<rightList.val:
            head=leftList
            head.next=self.mergetwoLists(leftList.next,rightList)
        else:
            head=rightList
            head.next=self.mergetwoLists(leftList,rightList.next)
        return head
            
if __name__=='__main__':
    list1=ListNode(7)
    list2=ListNode(49)
    list3=ListNode(73)
    list4=ListNode(32)
    list4nxt=ListNode(58)
    list4.next=list4nxt
    lists=[list1,list2,list3,list4]
    sol=Solution()
    print list4
    print sol.mergeKLists(lists)
     
