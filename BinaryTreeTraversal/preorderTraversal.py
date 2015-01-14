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
    def preorderTraversal(self, root):
        stack = []
        l = []
        d = {}
        if root == None:
            return []
        stack.append(root)
        while stack != []:
            current = stack[-1]
            if current.right != None and current.right not in d:
                stack.append(current.right)
                current = current.right
            else:
                if current.left != None and current.left not in d:
                    stack.append(current.left)
                    current = current.left
                else:
                    l.append(stack[-1].val)
                    d[stack[-1]] = True
                    stack.pop()
        l.reverse()
        return l
