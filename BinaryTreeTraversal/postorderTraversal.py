#! /usr/bin/python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        stack = []
        d = {}
        l = []
        if root == None:
            return []
        stack.append(root)
        while stack != []:
            current = stack[-1]
            if current.left != None and current.left not in d:
                stack.append(current.left)
                current = current.left
            else:
                if current.right != None and current.right not in d:
                    stack.append(current.right)
                    current = current.right
                else:
                    l.append(stack[-1].val)
                    d[stack[-1]] = True
                    stack.pop()
        return l
        
