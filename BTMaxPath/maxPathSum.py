#! /usr/bin/python

class TreeNode:
    def __init__(self,x):
	self.val=x
	self.left=None
	self.right=None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root==None:
            return 0
        sum1=self.maxPathSum(root.left)
        sum2=self.maxPathSum(root.right)
        sum3=root.val+self.rootleafMaxPath(root.left)+self.rootleafMaxPath(root.right)
	sum4=self.rootleafMaxPath(root)
        return max(sum1,sum2,sum3,sum4)
        
    def rootleafMaxPath(self,root):
        if root==None:
            return 0
        sum1=self.rootleafMaxPath(root.left)
        sum2=self.rootleafMaxPath(root.right)
        sum3=max(root.val,max(sum1,sum2)+root.val)
        return sum3

if __name__=="__main__":
    root=TreeNode(-1)
    left=TreeNode(-2)
    right=TreeNode(-3)
    root.left=left
    root.right=right
    s=Solution()
    print s.maxPathSum(root)
