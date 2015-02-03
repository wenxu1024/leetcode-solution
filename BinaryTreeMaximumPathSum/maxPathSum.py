#! /usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maximum = -9999
        self.maxRootPath(root)
        return self.maximum
        
        
    def maxRootPath(self, root):
        if root == None:
            return 0
        sum = root.val
        left = max(self.maxRootPath(root.left), 0)
        right = max(self.maxRootPath(root.right), 0)
        self.maximum = max(self.maximum, root.val + left + right)
        return max(root.val, root.val + left, root.val + right)
