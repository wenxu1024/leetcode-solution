# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root: return []
        lleft=self.levelOrder(root.left)
        lright=self.levelOrder(root.right)
        l=[[root.val]]
        length1=len(lleft)
        length2=len(lright)
        lmin= length1 if length1<length2 else length2
        for i in range(lmin) :
            level=lleft[i]+lright[i]
            l+=[level]
        if length1>length2:
            for i in range(lmin,length1):
                level=lleft[i]
                l+=[level]
        else:
            for i in range(lmin,length2):
                level=lright[i]
                l+=[level]
        return l
            
        
