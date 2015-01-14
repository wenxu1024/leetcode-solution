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
    def inorderTraversal(self, root):
        stack = []
        l =[]
        d = {}
        if root == None:
            return []
        current = root
        stack.append(current)
        while stack != []:
            current = stack[-1]
            if current.left != None and current.left not in d:
                stack.append(current.left)
                current = current.left
            else:
                l.append(stack[-1].val)
                temp = stack[-1]
                d[temp] = True
                stack.pop()
                if temp.right != None:
                    stack.append(temp.right)
        return l
            
